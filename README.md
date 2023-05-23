# 2023 Semestre 1

## Instrucciones Generales
- El archivo **debe** llamarse **Examen3.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- Deben contruir las funciones con **Python**
- Debe utilizar la programación solo por **recursión** 
- Debe crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**
- Recordar que en este caso por evaluar vectores o matrices **no se debe recortar**, solo el recorrido es por sus índices
- Pueden hacer uso **Try/Except, isinstance, type**
- Pueden hacer el uso de las funciones que se va creando durante el examen
- En todos los problemas aquí expuestos debe de validarse:
	-  de que los vectores acepten solo números enteros
	-  la matriz no debe ser nula
	-  deben ser homogéneas y del mismo largo
	-  los mensajes de error deben ser claros


## numeroHermano(num)

Escriba un programa con sintaxis Python cuya función principal se llame **numeroHermano(num)**, que reciba como entrada un **número entero positivo** denominado num y que retorne si cumple (True) o no los requisitos (False) de número hermano. Un número hermano es un número natural y que posee al menos dos divisores primos (el 1 no es primo):

Ejemplos del comportamiento de la función:

```python
>>>numeroHermano(20) #(divisores propios: 2, 4, 5, 10)
True
>>> numeroHermano(8) #(divisores propios: 2,4)
False
>>> numeroHermano(-8)
"Error en la entrada, debe ser número positivo"
```

## esVectorOrdenado(vector, forma)

Escriba un programa con sintaxis Python cuya función principal se llame **esVectorOrdenado(vector, forma)**, que reciba como entradas un **vector** y una **forma**, este último será un string que especificará si el vector está ordenado en forma **ascendente o descendente**. Esta función retornará **True** si el vector corresponde al tipo de ordenamiento o **False** del caso contrario. No se puede usar su representación inversa o reversa del número

Los valores para **forma** son:  'asc' o 'desc'

```python
>>> esVectorOrdenado([23, 656, 5533, 8120], 'asc')
True
>>> esVectorOrdenado([15, 4, 0], 'desc')
True
>>> esVectorOrdenado([11, 45], 'desc')
False
```

## digitoMayoryMenor(lista)

Escriba un programa con sintaxis Python cuya función principal se llame **digitoMayoryMenor(lista)**, que reciba como entrada una **lista** con número **enteros**, y que retorne una lista de nuevos números que estará compuesto por los dígitos mayor y menor del número analizado.

```python
>>> digitoMayoryMenor([2300, 6756])
[30, 76]
>>> digitoMayoryMenor([2300, 6756, -99, 1001, 91823])
[30, 76, -99, 10, 91]

```

## comprimirMatriz(matriz)
	
Escriba una solución con sintaxis Python cuya función principal se llame **comprimirMatriz(matriz)**, recibe como parámetro de entrada una matriz **válida** y lo que se debe realizar es retornar una matriz donde sus vectores o filas son el resultado de la suma de su vector adyacente, en el caso de que la matriz tenga filas impar, la última no será sumada:

matriz = [[2, 15], [8, 12], [5, 6], [30, 50]]

resultado = [[28, 27], [35, 56]]

![image](https://user-images.githubusercontent.com/1167750/167149485-583e0ab8-8991-4996-84c6-7af407327b24.png)


```python
>>> comprimirMatriz([[20, 15], [8, 12], [5, 6], [30, 50]])
[[28, 27], [35, 56]]

>>> comprimirMatriz([[2, 15, 2], [8, 12, 10], [5, 6, 0], [30, 50, 15], [5, 8, 6], [10, 12, 100]])
[[10, 27, 12], [35, 56, 15], [15, 20, 106]]

```
