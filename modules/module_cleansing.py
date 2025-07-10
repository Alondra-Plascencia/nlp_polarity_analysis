
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import re

# Definir la expresión regular fuera de la función para optimización
remover = re.compile('<.*?>')

# Definir la función para eliminar etiquetas HTML
def remover_html(text):
    # Usar la expresión regular compilada para reemplazar etiquetas HTML por texto vacío
    return re.sub(remover, '', text)

# Definir la función para remover caracteres no alfanuméricos usando re y tambien numeros sueltos dado que en un analisis de sentimiento un numero
#suelto no genera mayor intensidad a la exprecion negativa o positiva
def remover_no_alfanumericos(text):
    # Reemplazar todo lo que no sea alfanumérico por un espacio
    return re.sub(r'[^a-zA-Z]', ' ', text)
