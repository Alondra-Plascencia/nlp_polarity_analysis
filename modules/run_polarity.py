#Libraries

#Standard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

#SKLearn
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

#NLTK
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#Third party
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

#External Modules
from module_data_path import df_data_path, plot_data_path, import_csv
from module_cleansing import clean_and_lowercase_columns, clean_and_lowercase_rows

stages = [1]  # Define the stages to run

#Data Importing
def stage1(): 
    # Data files directory path
    data_path = df_data_path()

    # Load the headlines and comments data from CSV files
    data_df = import_csv(data_path,'DATA_PRUEBA.csv')

    # Clean and lowercase the headline text and all comment fields in the DataFrames
    start_col_index = 2  # Assuming the first three columns are not comments
    data_df = data_df.apply(clean_and_lowercase_rows, axis=1, start_col_index=start_col_index)

    # Preview the first 10 cleaned headlines and comments (optional)
    print(data_df.iloc[:,start_col_index:].head(10))
        
#Data Cleaning and Preprocessing
def stage2(): 
    print("Stage 2")


if __name__ == "__main__":

    if 1 in stages:
        stage1()
    elif 2 in stages:
        stage2()
