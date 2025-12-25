"""Visualisation graphique de la matrice"""
# Import de NumPy
import numpy as np

# Import de matplotlib pour l'affichage graphique
import matplotlib.pyplot as plt


def visualize_matrix(matrix: np.ndarray, title: str = "Visualisation de la matrice") -> None:
    """
    Affiche une matrice sous forme de carte thermique (heatmap)
    """
    # Création d'une nouvelle fenêtre graphique
    plt.figure()

    # Affichage des valeurs sous forme de couleurs
    plt.imshow(matrix, cmap="viridis")

    # Barre indiquant l'intensité des valeurs
    plt.colorbar()

    # Titre de la fenêtre
    plt.title(title)

    # Affichage à l'écran
    plt.show()
