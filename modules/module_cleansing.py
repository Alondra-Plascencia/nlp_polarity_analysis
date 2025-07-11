
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import re

# Precompiled regular expression to optimize HTML tag removal
remover = re.compile('<.*?>')

def remover_html(text):
    """
    Removes HTML tags from the given text.

    The function uses a precompiled regular expression to find and replace HTML tags with empty strings, effectively stripping any markup.

    :param text: The input string containing HTML content.
    :return: The cleaned text with HTML tags removed.
    """
    return re.sub(remover, '', text)

def remover_no_alfanumericos(text):
    """
    Removes all non-alphabetic characters and isolated numbers from the text.

    This function replaces any character that is not a letter (a-z, A-Z) with a space. It is designed for sentiment analysis, where standalone numbers do not usually add significant positive or negative intensity to expressions.

    :param text: The input string to be cleaned.
    :return: The cleaned string containing only alphabetic characters and spaces.
    """
    return re.sub(r'[^a-zA-Z]', ' ', text)
