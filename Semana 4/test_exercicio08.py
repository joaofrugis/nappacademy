import pytest
from exercicio08 import juros_compostos

def test_exercicio08_1():
    assert juros_compostos(100, 1, 12) == 112.68

def test_exercicio08_2():
    assert juros_compostos(100, 25, 12) == 1455.19

def test_exercicio08_3():
    assert juros_compostos(100, 50, 12) == 12974.63

def test_exercicio08_4():
    assert juros_compostos(100, 75, 12) == 82500.5