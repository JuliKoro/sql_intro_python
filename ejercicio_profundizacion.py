'''
SQL Introducción [Python]
Ejercicio de profundización
---------------------------
Autor: Julián Andrés Koroluk
Version: 0.1

Descripcion:
Solución del ejercicio del enunciado descripto en el archivo de
"ejercicio_profundizacion.md".
'''

__author__ = "Julián Andrés Koroluk"
__email__ = "julian.koroluk@outlook.com"
__version__ = "0.1"

import sqlite3
import matplotlib.pyplot as plt
import matplotlib.axes
import numpy as np


def fetch():
    '''Consultar datos

    Se consultan los datos de la DB 'heart.db' y se extrae especificamente los
    datos de la columna 'pulso' de la tabla 'sensor'.
    Retorna una lista de todos los pulsos cardícos obtenidos de la tabla.
    '''
    
    # Se conecta a la DB
    conn = sqlite3.connect('heart.db')
    
    # Se crea el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Se lee la columna 'pulso' de la tabla 'sensor'
    c.execute("SELECT pulso FROM sensor")
    data = c.fetchall()
    
    return data


def show(data):
    pass


def estadistica(data):
    pass


def regiones(data):
    pass


if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  regiones(data)