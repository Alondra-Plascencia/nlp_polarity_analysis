# ====================================
# Libraries
# ====================================

# Standard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

# Scikit-Learn
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# NLTK
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# Third party
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# External Modules
from module_data_path import df_data_path, plot_data_path, catalog_data_path, import_csv, save_dataframe_to_csv
from module_cleansing import clean_and_lowercase_columns, clean_and_lowercase_rows
from module_tokenization import remove_stopwords, stem_row
from module_polarization import generate_sentiment_summary_df

# ====================================
# Configuration
# ====================================

stages = [3]  # Define the stages to run

start_col_index = 2  # Assuming the first two columns are not text (headliners or comments)

# ====================================
# Stage 1: Data importing, cleaning and preprocessing
# ====================================

def stage1(): 
    """
    Loads the data, cleans it by removing non-alphanumeric characters,
    converts text to lowercase, and saves the cleaned CSV.
    """   
    # Get data and catalog paths
    data_path = df_data_path()
    catalog_path = catalog_data_path()

    # Load the raw CSV data
    data_df = import_csv(data_path,'DATA_PRUEBA.csv')

    # Clean and lowercase text fields from start_col_index onwards
    data_df = data_df.apply(clean_and_lowercase_rows, axis=1, start_col_index=start_col_index)

    # Optionally preview cleaned data
    # print(data_df.iloc[:,start_col_index:].head(10))
    
    # Save cleaned data
    save_dataframe_to_csv(data_df, catalog_path, 'cleaned_data')
        
# ====================================
# Stage 2: Data tokenization
# ====================================

def stage2(): 
    """
    Loads the cleaned CSV, removes stopwords, applies stemming,
    and saves the tokenized result as CSV.
    """
    # Get catalog path
    catalog_path = catalog_data_path()
    
    # Load cleaned CSV
    data_df = import_csv(catalog_path,'cleaned_data.csv')
    
    # Apply stopwords removal
    data_df = data_df.apply(remove_stopwords, axis=1, start_col_index=start_col_index)
    
    # Apply stemming
    data_df = data_df.apply(stem_row, axis=1, start_col_index=start_col_index)
    
    # Optionally preview tokenized data
    # print(data_df.iloc[:,start_col_index:].head(10))
    
    # Save tokenized data
    save_dataframe_to_csv(data_df, catalog_path, 'tokenized_data')

# ====================================
# Stage 3: Data polarization
# ====================================

def stage3():
    """
    Loads the tokenized CSV, applies a pre-trained model for sentiment analysis,
    and saves the results as CSV.
    """
    # Get catalog path
    catalog_path = catalog_data_path()
    
    # Load tokenized CSV
    data_df = import_csv(catalog_path,'tokenized_data.csv')

    # df es tu DataFrame original con ID, Headline y comentarios
    summary_df = generate_sentiment_summary_df(data_df,
                                          id_col='ID',
                                          headline_col='Headliner',
                                          start_col_index=3)
    
    # Optionally preview sentiment summary
    #print(summary_df.head(20))
    
    # Save sentiment results
    save_dataframe_to_csv(summary_df, catalog_path, 'polarized_data')

# ====================================
# Main
# ====================================

if __name__ == "__main__":

    if 1 in stages:
        stage1()
    elif 2 in stages:
        stage2()
    elif 3 in stages:
        stage3()
