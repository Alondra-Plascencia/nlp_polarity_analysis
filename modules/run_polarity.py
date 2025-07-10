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
from module_cleansing import remover_no_alfanumericos

stages = [1]

#Data Importing
def stage1(): 
    # data files directory path
    data_path = df_data_path()

    titulares_df = import_csv(data_path,'titulares_prueba.csv')
    comentarios_df = import_csv(data_path,'comentarios_prueba.csv')
    
    titulares_df['Tweet'] = titulares_df['Tweet'].apply(remover_no_alfanumericos).str.lstrip().str.lower()
    
    # Reemplaza 'titulares_df' con el DataFrame que estás utilizando
    for index, row in comentarios_df.iterrows():  # Recorremos cada fila
        for col in comentarios_df.columns[3:]:  # Recorremos las columnas a partir de la 3ra columna (índice 2)
            if pd.notna(row[col]):  # Verifica que el valor no sea NaN
                # Aplica las transformaciones a los valores que no son NaN
                comentarios_df.at[index, col] = remover_no_alfanumericos(row[col]).lstrip().lower()
        



#Data Cleaning and Preprocessing
def stage2(): 
    print("Stage 2")


if __name__ == "__main__":

    if 1 in stages:
        stage1()
    elif 2 in stages:
        stage2()
