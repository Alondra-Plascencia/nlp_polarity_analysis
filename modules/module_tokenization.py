# ====================================
# Libraries
# ====================================

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# External modules
from config import language


# Define the function to remove stopwords (without converting to lowercase)
def remove_stopwords(row, start_col_index=0):
    """
    Removes stopwords from all columns in a DataFrame row starting from start_col_index.
    Non-NaN cells are processed: words in stopwords are removed, result is returned as a list of words.
    
    Parameters:
    - row: pandas Series (a row of the DataFrame)
    - start_col_index: int, index of the first column to process
    
    Returns:
    - The modified row with stopwords removed from specified columns.
    """
    # Ensure that the stopwords are downloaded
    nltk.download('stopwords')
    # Load the stopwords only once
    stop_words = set(stopwords.words(language))
    for col in row.index[start_col_index:]:
        if pd.notna(row[col]):
            words = str(row[col]).split()
            cleaned_words = [word for word in words if word.lower() not in stop_words]
            row[col] = cleaned_words
    return row


# Define the function for word stemming
def stem_row(row, start_col_index=0):
    """
    Applies stemming to all text columns in a DataFrame row starting from start_col_index.
    Non-NaN cells are processed: each word is stemmed, result is returned as a list of words

    Parameters:
    - row: pandas Series (a row of the DataFrame)
    - start_col_index: int, index of the first column to process

    Returns:
    - The modified row with words stemmed in specified columns.
    """
    # Stemmer instance (loaded once)
    ps = PorterStemmer()
    for col in row.index[start_col_index:]:
        value = row[col]
        if value is not None and not (isinstance(value, float) and pd.isna(value)):
            if isinstance(value, list):
                words = value
            else:
                words = str(value).split()
            stemmed_words = [ps.stem(word) for word in words]
            row[col] = stemmed_words
    return row