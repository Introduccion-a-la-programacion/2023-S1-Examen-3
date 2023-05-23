import Examen3;
import pytest;

def test_esVectorOrdenado_1():
    assert Examen3.esVectorOrdenado([23, 656, 5533, 8120], 'asc') == True
    
def test_esVectorOrdenado_2():
    assert Examen3.esVectorOrdenado([15, 4, 0], 'desc') == True
    
def test_esVectorOrdenado_3():
    assert Examen3.esVectorOrdenado([11, 45], 'desc') == False
    
#################################################################

def test_digitoMayoryMenor_1():
    assert Examen3.digitoMayoryMenor([2300, 6756]) == [30, 75]
    
def test_digitoMayoryMenor_2():
    assert Examen3.digitoMayoryMenor([2300, 6756, -99, 1001, 91823]) == [30, 75, -99, 10, 91]
    
#################################################################

def test_comprimirMatriz_1():
    assert Examen3.comprimirMatriz([[2, 15], [8, 12], [5, 6], [30, 50]]) == [[10, 27], [35, 56]]

def test_comprimirMatriz_2():
    assert Examen3.comprimirMatriz([[2, 15, 2], [8, 12, 10], [5, 6, 0], [30, 50, 15], [5, 8, 6], [10, 12, 100]]) == [[10, 27, 12], [35, 56, 15], [15, 20, 106]]
    
#################################################################    

def test_numeroHermano_1():
    assert Examen3.numeroHermano(20) == True
    
def test_numeroHermano_2():
    assert Examen3.numeroHermano(8) == False
    
def test_numeroHermano_3():
    assert isinstance(str(Examen3.numeroHermano(-8)), str) == isinstance("Error: Número debe ser positivo", str)
