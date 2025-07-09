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
from module_data_path import df_data_path, plot_data_path

stages = [1]

#Data Importing
def stage1(): 
    # data files directory path
    data_path = df_data_path()

    titulares_df = os.path.join(data_path, 'titulares_prueba.csv')
    coments_df = os.path.join(data_path, 'comentarios_prueba.csv')
    print('Stage 1')




#Data Cleaning and Preprocessing
def stage2(): 
    print("Stage 2")


if __name__ == "__main__":

    if 1 in stages:
        stage1()
    elif 2 in stages:
        stage2()
