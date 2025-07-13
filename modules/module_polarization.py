from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
from module_cleansing import remove_non_alphabetic

# This model could also be used, designed for Spanish only; it is lighter. (language = 'spanish')
# This model only has 3 polarities.
model_name = "pysentimiento/robertuito-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Function to predict sentiment using the robertuito model
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
            # Apply transformations to non-NaN values
            row[col] = predict_sentiment_robertuito_model(str(row[col]))
    return row

def generate_sentiment_summary_df(df, id_col='ID', headline_col='Headline', start_col_index=2):
    """
    Crea un DataFrame con:
    - columna ID
    - columna Headline
    - neg_count: número de comentarios negativos
    - neu_count: número de comentarios neutros
    - pos_count: número de comentarios positivos

    Parámetros:
    - df: DataFrame original con columnas [ID, Headline, comentario1, comentario2, …]
    - id_col: nombre de la columna de identificador
    - headline_col: nombre de la columna de titulares
    - start_col_index: índice de la primera columna de comentarios
    """
    # 1) Predecir sentimientos en cada fila
    sentiments = df.apply(lambda row: predict_sentiment_robertuito(row, start_col_index), axis=1)

    # 2) Contar cada polaridad fila por fila
    summary_rows = []
    for _, row in sentiments.iterrows():
        counts = row[row.index[start_col_index:]].value_counts()
        summary_rows.append({
            id_col:            row[id_col],
            headline_col:      row[headline_col],
            'neg_count':       counts.get('NEG', 0),
            'neu_count':       counts.get('NEU', 0),
            'pos_count':       counts.get('POS', 0)
        })

    # 3) Crear el DataFrame resumen
    return pd.DataFrame(summary_rows)

# This model performs multilingual sentiment analysis and outputs one of five classes.
# It is heavier than language-specific lightweight models.
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
    labels = ["Muy Negativo", "Negativo", "Neutro", "Positivo", "Muy Positivo"]
    return labels[sentiment]

def generate_sentiment_summary_df_5categories(
    df,
    id_col='ID',
    headline_col='Headline',
    start_col_index=2
):
    """
    Crea un DataFrame resumen con:
      - ID
      - Headline
      - muy_negativo_count: nº de comentarios 'Muy Negativo'
      - negativo_count:     nº de comentarios 'Negativo'
      - neutro_count:       nº de comentarios 'Neutro'
      - positivo_count:     nº de comentarios 'Positivo'
      - muy_positivo_count: nº de comentarios 'Muy Positivo'
    
    Parámetros:
      - df: DataFrame original con [ID, Headline, comentario1, comentario2, …]
      - id_col: nombre de la columna de ID
      - headline_col: nombre de la columna de titular
      - start_col_index: índice (0-based) donde empiezan las columnas de comentarios
    """
    import pandas as pd

    # 1) Aplicar la predicción de sentimiento a cada celda de comentario
    df_sent = df.copy()
    for col in df_sent.columns[start_col_index:]:
        df_sent[col] = df_sent[col].apply(
            lambda tokens: predict_sentiment(tokens) if pd.notna(tokens) else tokens
        )

    # 2) Definir categorías y contarlas por fila
    categories = ["Muy Negativo", "Negativo", "Neutro", "Positivo", "Muy Positivo"]
    summary_rows = []
    for _, row in df_sent.iterrows():
        counts = row.iloc[start_col_index:].value_counts()
        # Construir fila de resumen
        summary_rows.append({
            id_col: row[id_col],
            headline_col: row[headline_col],
            'muy_negativo_count': counts.get("Muy Negativo", 0),
            'negativo_count':     counts.get("Negativo", 0),
            'neutro_count':       counts.get("Neutro", 0),
            'positivo_count':     counts.get("Positivo", 0),
            'muy_positivo_count': counts.get("Muy Positivo", 0),
        })

    # 3) Devolver DataFrame ordenado
    cols = [
        id_col,
        headline_col,
        'muy_negativo_count',
        'negativo_count',
        'neutro_count',
        'positivo_count',
        'muy_positivo_count'
    ]
    return pd.DataFrame(summary_rows, columns=cols)



