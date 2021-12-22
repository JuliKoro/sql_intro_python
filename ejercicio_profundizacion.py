'''
SQL Introducción [Python]
Ejercicio de profundización
---------------------------
Autor: Julián Andrés Koroluk
Version: 1.0

Descripcion:
Solución del ejercicio del enunciado descripto en el archivo de
"ejercicio_profundizacion.md".
'''

__author__ = "Julián Andrés Koroluk"
__email__ = "julian.koroluk@outlook.com"
__version__ = "1.0"

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
        f'Desvío estandar: {desvio} ppm\n')


def regiones(data):
    '''Categorizar Ritmos Cardíacos

    Separa los datos de ritmos cardíacos en tres categorías (aburrido, tranquilo y entusiasmado)
    segun el nivel de intesnsidad con respecto al ritmo cardíaco promedio con el desvío.
    Luego realiza un gráfico de disperción de las tres categorías.

    @param List data Rítmos cardíacos
    '''

    prom = np.mean(data)
    desvio = np.std(data)

    x1 = [] # Estado aburrido
    y1 = []
    x2 = [] # Estado entusiasmado
    y2 = []
    x3 = [] # Estado tranquilo
    y3 = []
    for i in range(len(data)):
        if data[i] <= (prom-desvio): # Estado aburrido
            x1.append(i)
            y1.append(data[i])
        elif data[i] >= (prom-desvio): # Estado entusiasmado
            x2.append(i)
            y2.append(data[i])
        else: # Estado tranquilo
            x3.append(i)
            y3.append(data[i])

    fig = plt.figure(facecolor='whitesmoke')
    fig.suptitle('Estados de la persona', fontsize=16)
    ax = fig.add_subplot()
    ax.scatter(x1, y1, c='blueviolet', alpha=0.2, label='aburrido')
    ax.scatter(x2, y2, c='tomato', alpha=0.2, label='entusiasmado')
    ax.scatter(x3, y3, c='turquoise', alpha=0.2,  label='tranquilo')
    ax.axhline(prom, c='black', label='promedio')
    ax.axhline((prom+desvio), c='darkgrey', linestyle='--', label='desvío')
    ax.axhline((prom-desvio), c='darkgrey', linestyle='--')

    ax.set_ylabel('pulsaciones por minuto [ppm]', c='black', fontweight='bold')
    ax.legend()

    print('Gráfico distintos estados cardíacos:')
    plt.show()


if __name__ == "__main__":
    print('Bienvenidos!\nEste programa realiza un analicis de datos sobre el ritmo cardíaco de una persona mirando un partido de fútbol.\n')    

    # Leer la DB
    data = fetch()

    # Data analytics
    show(data)
    estadistica(data)
    regiones(data)