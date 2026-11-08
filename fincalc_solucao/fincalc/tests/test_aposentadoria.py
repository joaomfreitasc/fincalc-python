import pytest

from fincalc import calcular_aposentadoria


def test_aposentadoria_padrao():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    # Assert
    assert round(patrimonio, 2) == 265277.59


def test_aposentadoria_tempo_zero():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 0, 6.0)
    # Assert
    assert round(patrimonio, 2) == 10000.00


def test_aposentadoria_taxa_zero():
    # Arrange & Act
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 1, 0.0)
    # Assert
    assert round(patrimonio, 2) == 16000.00


def test_aposentadoria_patrimonio_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_aposentadoria(-1.0, 500.0, 10, 6.0)


def test_aposentadoria_aporte_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_aposentadoria(10000.0, -500.0, 10, 6.0)


def test_aposentadoria_tempo_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_aposentadoria(10000.0, 500.0, -1, 6.0)
