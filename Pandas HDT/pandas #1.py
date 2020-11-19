#Universidad del Valle de Guatemala
#Algoritmos y Programación básica
#Eduardo Rubin 20291

#import csv
import pandas as pd
#import numpy as np
import matplotlib as mat
#import requests as req


#print(dir(pd)) directorio de funciones de pandas

archivo = "/Users/Andrés Armira/Desktop/costo_de_vida.csv"

with open(archivo, "r", encoding = "utf-8") as hoja: #verificar que el archivo CSV se puede leer correctamente
    
    print("\n" + "Se ha cargado el archivo correctamente" + "\n")
   
read = pd.read_csv(archivo) #leer el archivo CSV como un archivo dentro de pandas
df = pd.DataFrame(read) #encontrar el dataframe del archivo

menu = ("\n" + "1. Número de filas y columnas" + "\n" +
        "2. Tipos de variables" + "\n" +
        "3. Datos faltantes" + "\n" +
        "4. Estadíticas básicas" + "\n" +
        "5. Salir del programa")
print(menu)
    
res = input("Seleccione el índice con la acción que desea realizar: ")
b = True

while b == True:
    
    a = True

    while a == True:  
        try:
            res2 = int(res)
            if 0 < res2 < 6:
                a = False
                
            else:
                print("Error: número inválido")
                res = input("Seleccione el índice con la acción que desea realizar: ")
    
        except ValueError:
            print("Error: código inválido")
            res = input("Seleccione el índice con la acción que desea realizar: ")
        
    if res2 == 1:  

        print("\n" + "                     El número de filas y columnas es:")
        print("-----------------------------------------------------------------------------")
        print(df) #DataFrame del documentos CSV 
        print("\n" + "El documento cuenta con dimensiones de " + str(len(df)) + " filas y " + str(read.shape[1]) + " columnas")
        
        print(menu)
        res = input("Seleccione el índice con la acción que desea realizar: ")
        
    if res2 == 2:
        print("\n" + "                     Los tipos de variables son:")
        print("------------------------------------------------------------------------------" + "\n")
        print(str(read.dtypes)) #información de las columnas del documento

        print(menu)
        res = input("Seleccione el índice con la acción que desea realizar: ")
        
    if res2 == 3:
        print("\n" + "                    La estructura del documento es: ")
        print("------------------------------------------------------------------------------" + "\n")
        print(read.head()) #dropna bota las filas sin espacios y quiero todas las filas disponibles 
        print("\n" + "Los datos faltantes son los descritos con el código NaN")

        print(menu)
        res = input("Seleccione el índice con la acción que desea realizar: ")
    
    if res2 == 4:
        print("\n" + "         Las estadísticas básicas son: ")
        print("-------------------------------------------------" + "\n")
        print(read.describe())
        
        print(menu)
        res = input("Seleccione el índice con la acción que desea realizar: ")
        
    if res2 == 5:
        b = False
        exit()

print("------------------------------------------------------------------------------" + "\n")

#No. de columnas: len(read_csv)
#No. de filas: read_csv.shape[1]
#Tipos de varibles: .info() y .dtypes()
#Datos faltantes: "NaN" y .dropna()

