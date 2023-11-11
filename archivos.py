# -*- coding: utf-8 -*-
"""archivos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15JrYEOW_jSKcn8vJnYlX6P1yUEqtAsOq
"""

from csv import reader
import math as m
import statistics as stat
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Xi = []
Yi = []

U = pd.read_csv("datos.txt", names = ["x", "y"] )

print(U)

print(U["x"])


# importante: cambiar estaturas.txt por el archivo correspondiente
with open("datos.txt", 'r') as archivo_lectura:
    csv = reader(archivo_lectura)
    # ir fila a fila
    for linea in csv:
        # hacer algo con cada fila, asumo que cada fila tiene un solo valor
        print(linea)
        Xi.append(float(linea[0]))
        Yi.append(float(linea[1]))
        ## recordar el split

X = np.array(Xi)
Y = np.array(Yi)

sumx = sum(X)
sumy = sum(Y)
sumxy = sum(X*Y)
sumx2 = sum(X**2)
n = len(X)

print(sumx2)
print(sumxy)

A = (n*sumxy - (sumx*sumy)) / (n*sumx2 - sumx**2)
B = (sumy - A*sumx) /n

X2 = np.linspace(0, 10, n)
Y2 = A*X2 + B

plt.plot(X, Y, "ob")
plt.plot(X2, Y2, "r")

print(A)
print(B)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile leerArchivo.cpp
# 
# #include <iostream>
# #include <fstream>
# #include <vector>
# #include <sstream>
# 
# using namespace std;
# 
# 
# int main(int argc, char** argv)
# {
#     vector<double> X, Y;
#     string nombre, linea;
#     nombre = "datos.txt";
#     ifstream archivo;
#     archivo.open(nombre);
#     int contLineas = 0;
#     int n;
#     if (!archivo)
#     {
#         cout << "Archivo inválido.";
#     }
#     else
#     {
#     while (getline(archivo, linea))
#         {
#             contLineas++;
#             // Se imprime la línea completa
#             cout << "Linea número " << contLineas << " : " << linea << endl;
#             // Acá se divide la línea por los separadores
#         
#             char separador = ',';
#             stringstream ssLinea(linea);
#             string token;
#             // acá se separa cada linea en los elementos entre los puntos y coma
#             int cont = 0;
#             while (getline(ssLinea, token, separador))
#             {
#                 if (cont == 0) X.push_back(stof(token));
#                 if (cont == 1) Y.push_back(stof(token));
#                 cout << token << endl;
#                 cont++;
#             } 
#             //listado.push_back(elemento);
#             // acá se arma el registro entero, es un <<listado>> de <<elementos>>
#         }
# 
#     double sumx = 0.0, sumy = 0.0, sumxy = 0.0, sumx2 = 0.0, A, B;
#     
# 
#     n = X.size();
# 
#     for (int i = 0; i < n; i++)
#     {
#         sumx = sumx + X[i];
#         sumy = sumy + Y[i];
#         sumxy = sumxy + X[i]*Y[i];
#         sumx2 = sumx2 + X[i]*X[i];
#     }
#     A = (n*sumxy - (sumx*sumy)) / (n*sumx2 - sumx*sumx);
#     B = (sumy - A*sumx) /n;
#     cout << "Valor de A: " << A <<  " , valor de B: " << B << std::endl; 
#     cout << "Escribiendo " << contLineas << " registros..." << endl;
#     ofstream archivoS;
#     archivoS.open("salida.txt");
#     double dx = (10. - 0.) / n;
#     double valor = 0.0;
#     for (int i = 0; i < n; i++)
#     {
#         valor = A * (i*dx) + B;
#         archivoS << i*dx << ", " << valor << endl;
#     } 
#     }
# 
# 
#     
# 
# }

!g++ -o leerArchivo leerArchivo.cpp

!./leerArchivo