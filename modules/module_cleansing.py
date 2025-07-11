
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
import unicodedata2

# Precompiled regular expression to optimize HTML tag removal
remove = re.compile('<.*?>')

def remove_html(text):
    """
    Removes HTML tags from the given text.

    The function uses a precompiled regular expression to find and replace HTML tags with empty strings, effectively stripping any markup.

    :param text: The input string containing HTML content.
    :return: The cleaned text with HTML tags removed.
    """
    return re.sub(remove, '', text)

def remove_non_alphabetic(text):
    """
    Removes all non-alphabetic characters and isolated numbers from the text.

    This function replaces any character that is not a letter (a-z, A-Z) with a space. It is designed for sentiment analysis, where standalone numbers do not usually add significant positive or negative intensity to expressions.

    :param text: The input string to be cleaned.
    :return: The cleaned string containing only alphabetic characters and spaces.
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
        return remove_non_alphabetic(col).lower().lstrip()
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
            row[col] = remove_non_alphabetic(str(row[col])).lstrip().lower()
    return row