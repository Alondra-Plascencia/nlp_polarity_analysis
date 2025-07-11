
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
import unicodedata2

# Definir la expresión regular fuera de la función para optimización
remover = re.compile('<.*?>')

# Definir la función para eliminar etiquetas HTML
def remover_html(text):
    # Usar la expresión regular compilada para reemplazar etiquetas HTML por texto vacío
    return re.sub(remover, '', text)

# Definir la función para remover caracteres no alfanuméricos usando re y tambien numeros 
# sueltos dado que en un analisis de sentimiento un numero suelto no genera mayor intensidad 
# a la exprecion negativa o positiva
def remover_no_alfanumericos(text):
    """
    Reemplazar todo lo que no sea alfanumérico por un espacio
    """
    text = unicodedata2.normalize('NFC', text)
    return re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]', ' ', text)

def clean_and_lowercase_columns(col):
    """
    Cleans and lowercases all text values in a DataFrame column.

    For each non-null string in the column, this function:
    - Removes non-alphabetic characters (while preserving accented letters and 'ñ').
    - Strips leading whitespace.
    - Converts the text to lowercase.

    Parameters:
        col (pd.Series): The column to process.

    Returns:
        pd.Series: The cleaned column.
    """
    if isinstance(col, str):
        return remover_no_alfanumericos(col).lower().lstrip()
    return col

def clean_and_lowercase_rows(row, start_col_index=2):
    """
    Cleans and lowercases text fields in a DataFrame row.

    Starting from the specified column index, this function:
    - Removes non-alphabetic characters (while keeping accented letters and 'ñ').
    - Strips leading whitespace.
    - Converts text to lowercase.

    Parameters:
        row (pd.Series): A row from the DataFrame.
        start_col_index (int): Index of the first column to process.

    Returns:
        pd.Series: The cleaned row.
    """
    # Iterate over all columns starting from the specified index
    for col in row.index[start_col_index:]:
        if pd.notna(row[col]):  # Check that the value is not NaN
            # Apply transformations to non-NaN values
            row[col] = remover_no_alfanumericos(str(row[col])).lstrip().lower()
    return row



