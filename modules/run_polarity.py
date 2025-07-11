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
from module_cleansing import remover_no_alfanumericos, clean_and_lowercase_columns, clean_and_lowercase_rows

stages = [1]

#Data Importing
def stage1(): 
    # data files directory path
    data_path = df_data_path()

    headliners_df = import_csv(data_path,'titulares_prueba.csv')
    coments_df = import_csv(data_path,'comentarios_prueba.csv')
    

    headliners_df['Tweet'] = headliners_df['Tweet'].apply(clean_and_lowercase_columns)
    start_col_index = 3  # Assuming the first three columns are not comments
    coments_df = coments_df.apply(clean_and_lowercase_rows, axis=1, start_col_index=start_col_index)

    #print(headliners_df['Tweet'].head(10))
    #print(coments_df.iloc[:, 3:].head(10))
        
#Data Cleaning and Preprocessing
def stage2(): 
    print("Stage 2")


if __name__ == "__main__":

    if 1 in stages:
        stage1()
    elif 2 in stages:
        stage2()
