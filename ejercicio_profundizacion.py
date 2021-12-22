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

    print('¡Consulta a la DB con éxito!')

    return data


def show(data):
    '''Visualización de datos

    Realiza un gráfico de línea en base a la evolución del rítmo cardíaco.

    @param List data Rítmos cardíacos
    '''
    
    y = list(range(len(data)))

    fig = plt.figure(facecolor='whitesmoke')
    fig.suptitle('Evolución del ritmo cardíaco', fontsize=16)
    ax = fig.add_subplot()
    ax.plot(y, data, color='darkred', label='Rítmo cardíaco')
    ax.set_ylabel('[ppm]', c='black', fontweight='bold')
    ax.legend()

    print('Gráfico de la Evolución Cardíaca:')
    plt.show()


def estadistica(data):
    '''Estadísticas de datos

    Calcula distinos valores estadísticos y los muestra.

    @param List data Rítmos cardíacos
    '''
    print('Estadísticas de la medición:\n')
    promedio = np.mean(data)
    min = np.min(data)
    max = np.max(data)
    desvio = np.std(data)
    print(f'Valor promedio: {promedio} ppm\n',
        f'Valor mínimo: {min} ppm\n',
        f'Valor máximo: {max} ppm\n',
        f'Desvío estandar: {desvio} pp,\n')


def regiones(data):
    pass


if __name__ == "__main__":
    print('Bienvenidos!\nEste programa realiza un analicis de datos sobre el ritmo cardíaco de una persona mirando un partido de fútbol.\n')    

    # Leer la DB
    data = fetch()

    # Data analytics
    show(data)
    estadistica(data)
    regiones(data)