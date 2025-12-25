"""Validation des entrées + surlignage des erreurs"""
# Import de NumPy pour créer des tableaux
import numpy as np

# Import du widget Text de Tkinter
from tkinter import Text


def parse_matrix(text: str) -> np.ndarray:
    """
    Convertit un texte en matrice NumPy
    """
    # Liste pour stocker les lignes de la matrice
    rows = []

    # Découpage du texte ligne par ligne
    for line in text.strip().splitlines():
        # Conversion de chaque valeur en float
        rows.append([float(value) for value in line.split()])

    # Transformation en tableau NumPy
    return np.array(rows)


def highlight_error(widget: Text) -> None:
    """
    Met en évidence une erreur de saisie (fond rouge clair)
    """
    widget.configure(bg="#ffcccc")


def clear_highlight(widget: Text) -> None:
    """
    Réinitialise la couleur du champ après correction
    """
    widget.configure(bg="white")
