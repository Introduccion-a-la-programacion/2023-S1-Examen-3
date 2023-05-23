# 2022 Semestre 1
# Segundo Examen [Video](https://web.microsoftstream.com/video/2e33e280-916d-484a-8e2d-b307b5a7ca26)

## Instrucciones Generales
- El archivo **debe** llamarse **Examen2.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación solo por **iteración** en **todos** sus métodos, es decir el uso de **While o For**
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Recordar que en este caso por evaluar vectores o matrices no se debe recortar, solo el recorrido es por sus índices
- Pueden hacer uso **Try/Except, isinstance, type**
- Pueden hacer el uso de las funciones como **largoLista, validarVector, esMatrizCuadrada**
- En todos los problemas aquí expuestos debe de validarse:
	-  de que los vectores acepten solo números enteros
	-  la matriz no debe ser nula
	-  deben ser homogéneas y del mismo largo
	-  los mensajes de error deben ser claros


## esVectorOrdenado(vector, forma)

Escriba un programa con sintaxis Python cuya función principal se llame **esVectorOrdenado(vector, forma)**, que reciba como entradas un **vector** y una **forma**, este último será un string que especificará si el vector está ordenado en forma **ascendente o descendente**. Esta función retornará **True** si el vector corresponde al tipo o **False** del caso contrario

Los valores para **forma** son:  'asc' o 'desc'

```python
>>> esVectorOrdenado([23, 656, 5533, 8120], 'asc')
True
>>> esVectorOrdenado([15, 4, 0], 'desc')
True
>>> esVectorOrdenado([11, 45], 'desc')
False
```

## separarDigitos(lista)

Escriba un programa con sintaxis Python cuya función principal se llame **separarDigitos(lista)**, que reciba como entrada una **lista** con número **enteros positivos** desde 1000 hasta 9999 inclusive, y que retorne una matriz donde cada fila de estará compuesto por los dígitos por separado de cada número de la lista del parámetro de entrada.

```python
>>> separarDigitos([2300, 6756])
[[2,3,0,0], [6,7,5,6]]
>>> separarDigitos([1520, 4500, 6000])
[[1,5,2,0], [4,5,0,0], [6,0,0,0]]

```

## comprimirMatriz(matriz)
	
Escriba una solución con sintaxis Python cuya función principal se llame **comprimirMatriz(matriz)**, recibe como parámetro de entrada una matriz con un número de **filas par**,  no hay restricción con el número de columnas. Lo que se debe realizar es retornar una matriz donde sus vectores o filas son el resultado de la suma de cada dos filas de la matriz inicial, es decir:

matriz = [[2, 15], [8, 12], [5, 6], [30, 50]]

resultado = [[28, 27], [35, 56]]

![image](https://user-images.githubusercontent.com/1167750/167149485-583e0ab8-8991-4996-84c6-7af407327b24.png)


```python
>>> comprimirMatriz([[20, 15], [8, 12], [5, 6], [30, 50]])
[[28, 27], [35, 56]]

>>> comprimirMatriz([[2, 15, 2], [8, 12, 10], [5, 6, 0], [30, 50, 15], [5, 8, 6], [10, 12, 100]])
[[10, 27, 12], [35, 56, 15], [15, 20, 106]]

```

## invertirMatriz(lista) 
Escriba una solución con sintaxis Python cuya función principal se llame **invertirMatriz(matriz)**, recibe como parámetro de entrada una matriz y debe devolver esa misma matriz pero invirtiendo los valores de columnas a filas

Ejemplo:

![image](https://user-images.githubusercontent.com/1167750/167147445-89c6111d-0bba-4488-86f3-bc029d4f966e.png)

![image](https://user-images.githubusercontent.com/1167750/167148137-011325a3-b7e9-4037-864b-2df25a282989.png)


```python
>>>invertirMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
[[1,5,9],[2,6,10],[3,7,11],[4,8,12]]

>>>invertirMatriz([[20, 15],[8, 12],[30, 50]])
[[20,8,30], [15,12,50]]
```
