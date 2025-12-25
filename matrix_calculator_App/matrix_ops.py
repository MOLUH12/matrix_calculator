"""Cette partie du code contient toute la logique mathématique (NumPy)"""

# Import de NumPy pour la manipulation des matrices
import numpy as np

# Union permet d'accepter plusieurs types numériques (int ou float)
from typing import Union


def add(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Addition de deux matrices A + B
    """
    # NumPy vérifie automatiquement la compatibilité des dimensions
    return a + b


def subtract(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Soustraction de deux matrices A - B
    """
    return a - b


def multiply(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Multiplication matricielle A × B
    """
    # L'opérateur @ est dédié à la multiplication matricielle
    return a @ b


def divide(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Division matricielle définie comme : A × B⁻¹
    """
    # Vérifie que B est une matrice carrée
    if b.shape[0] != b.shape[1]:
        raise ValueError("La matrice B doit être carrée pour la division")

    # Calcul de l'inverse de B
    inverse_b = np.linalg.inv(b)

    # Multiplication de A par l'inverse de B
    return a @ inverse_b


def determinant(a: np.ndarray) -> float:
    """
    Calcul du déterminant d'une matrice
    """
    # Le déterminant n'existe que pour les matrices carrées
    if a.shape[0] != a.shape[1]:
        raise ValueError("La matrice doit être carrée")

    # Conversion du résultat NumPy en float Python
    return float(np.linalg.det(a))


def inverse(a: np.ndarray) -> np.ndarray:
    """
    Calcul de l'inverse d'une matrice
    """
    if a.shape[0] != a.shape[1]:
        raise ValueError("La matrice doit être carrée")

    return np.linalg.inv(a)


def transpose(a: np.ndarray) -> np.ndarray:
    """
    Transposition d'une matrice
    """
    # .T est la syntaxe NumPy pour la transposée
    return a.T


def scalar_multiply(a: np.ndarray, scalar: Union[int, float]) -> np.ndarray:
    """
    Multiplication d'une matrice par un scalaire
    """
    return scalar * a
