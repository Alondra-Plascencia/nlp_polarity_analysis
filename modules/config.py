"""
config.py

This module defines global configuration variables for the polarity analysis project.
It centralizes key parameters so they can be easily managed and modified in one place.

Defined parameters:
--------------------
- language (str): the language used to load NLTK stopwords.
  Must be one of the supported NLTK languages.
  This value will be used during text cleaning to remove stopwords in the selected language.
"""

# Language for NLTK stopwords
'''
"arabic", "azerbaijani", "danish", "dutch", "english", "finnish", "french", "german", "greek",
"hungarian", "indonesian", "italian", "kazakh", "nepali", "norwegian", "portuguese", "romanian", 
"russian", "spanish", "swedish", "turkish".
'''
language = 'spanish' 