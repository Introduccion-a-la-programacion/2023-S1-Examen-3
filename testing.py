import Examen2;
import pytest;

def test_esVectorOrdenado_1():
    assert Examen2.esVectorOrdenado([23, 656, 5533, 8120], 'asc') == True
    
def test_esVectorOrdenado_2():
    assert Examen2.esVectorOrdenado([15, 4, 0], 'desc') == True
    
def test_esVectorOrdenado_3():
    assert Examen2.esVectorOrdenado([11, 45], 'desc') == False
    
#################################################################

def test_separarDigitos_1():
    assert Examen2.separarDigitos([2300, 6756]) == [[2,3,0,0], [6,7,5,6]]
    
def test_separarDigitos_2():
    assert Examen2.separarDigitos([1520, 4500, 6000]) == [[1,5,2,0], [4,5,0,0], [6,0,0,0]]
    
#################################################################

def test_comprimirMatriz_1():
    assert Examen2.comprimirMatriz([[2, 15], [8, 12], [5, 6], [30, 50]]) == [[10, 27], [35, 56]]

def test_comprimirMatriz_2():
    assert Examen2.comprimirMatriz([[2, 15, 2], [8, 12, 10], [5, 6, 0], [30, 50, 15], [5, 8, 6], [10, 12, 100]]) == [[10, 27, 12], [35, 56, 15], [15, 20, 106]]
    
#################################################################    

def test_invertirMatriz_1():
    assert Examen2.invertirMatriz([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]

def test_invertirMatriz_2():
    assert Examen2.invertirMatriz([[20, 15],[8, 12],[30, 50]]) == [[20,8,30], [15,12,50]]
