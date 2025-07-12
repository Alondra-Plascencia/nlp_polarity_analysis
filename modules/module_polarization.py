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



