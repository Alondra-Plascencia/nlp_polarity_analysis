from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
from module_cleansing import remove_non_alphabetic

# This model is designed specifically for Spanish; it is lighter and faster.
# It outputs only 3 polarities.
model_name = "pysentimiento/robertuito-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment using the RoBERTuito model
def predict_sentiment_robertuito_model(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    labels = ["NEG", "NEU", "POS"]
    return labels[prediction]

def predict_sentiment_robertuito(row, start_col_index=2):
    for col in row.index[start_col_index:]:
        if pd.notna(row[col]):  # Check that the value is not NaN
            # Apply prediction only to non-NaN values
            row[col] = predict_sentiment_robertuito_model(str(row[col]))
    return row

def generate_sentiment_summary_df(df, id_col='ID', headline_col='Headline', start_col_index=2):
    """
    Creates a summary DataFrame with:
    - ID column
    - Headline column
    - neg_count: number of negative comments
    - neu_count: number of neutral comments
    - pos_count: number of positive comments

    Parameters:
    - df: Original DataFrame with columns [ID, Headline, comment1, comment2, …]
    - id_col: name of the ID column
    - headline_col: name of the headline column
    - start_col_index: index of the first comment column
    """
    # 1) Predict sentiment for each row
    sentiments = df.apply(lambda row: predict_sentiment_robertuito(row, start_col_index), axis=1)

    # 2) Count polarities for each row
    summary_rows = []
    for _, row in sentiments.iterrows():
        counts = row[row.index[start_col_index:]].value_counts()
        summary_rows.append({
            id_col:       row[id_col],
            headline_col: row[headline_col],
            'neg_count':  counts.get('NEG', 0),
            'neu_count':  counts.get('NEU', 0),
            'pos_count':  counts.get('POS', 0)
        })

    # 3) Create and return summary DataFrame
    return pd.DataFrame(summary_rows)


# This model performs multilingual sentiment analysis and outputs one of five classes.
# It is heavier than lightweight language-specific models.
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment from tokenized input (0–4):
# 0 → Very Negative, 1 → Negative, 2 → Neutral, 3 → Positive, 4 → Very Positive
def predict_sentiment(tokens):
    text = " ".join(tokens)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    sentiment = torch.argmax(outputs.logits, dim=1).item()
    labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
    return labels[sentiment]

def generate_sentiment_summary_df_5categories(
    df,
    id_col='ID',
    headline_col='Headline',
    start_col_index=2
):
    """
    Creates a summary DataFrame with:
      - ID
      - Headline
      - very_negative_count: number of 'Very Negative' comments
      - negative_count:      number of 'Negative' comments
      - neutral_count:       number of 'Neutral' comments
      - positive_count:      number of 'Positive' comments
      - very_positive_count: number of 'Very Positive' comments
    
    Parameters:
      - df: Original DataFrame with [ID, Headline, comment1, comment2, …]
      - id_col: name of the ID column
      - headline_col: name of the headline column
      - start_col_index: 0-based index where comment columns start
    """
    df_sent = df.copy()

    # 1) Apply sentiment prediction to each comment cell
    for col in df_sent.columns[start_col_index:]:
        df_sent[col] = df_sent[col].apply(
            lambda tokens: predict_sentiment(tokens) if pd.notna(tokens) else tokens
        )

    # 2) Define categories and count them per row
    categories = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
    summary_rows = []
    for _, row in df_sent.iterrows():
        counts = row.iloc[start_col_index:].value_counts()
        summary_rows.append({
            id_col: row[id_col],
            headline_col: row[headline_col],
            'very_negative_count': counts.get("Very Negative", 0),
            'negative_count':      counts.get("Negative", 0),
            'neutral_count':       counts.get("Neutral", 0),
            'positive_count':      counts.get("Positive", 0),
            'very_positive_count': counts.get("Very Positive", 0),
        })

    # 3) Return ordered summary DataFrame
    cols = [
        id_col,
        headline_col,
        'very_negative_count',
        'negative_count',
        'neutral_count',
        'positive_count',
        'very_positive_count'
    ]
    return pd.DataFrame(summary_rows, columns=cols)
