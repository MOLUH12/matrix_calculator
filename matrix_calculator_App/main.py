"""Point d’entrée du programme"""
# Import de Tkinter
import tkinter as tk

# Import de l'interface graphique
from ui import MatrixCalculatorUI


def main() -> None:
    # Création de la fenêtre principale
    root = tk.Tk()

    # Initialisation de l'application
    app = MatrixCalculatorUI(root)

    # Lancement de la boucle principale Tkinter
    root.mainloop()


# Exécution du programme
if __name__ == "__main__":# Cette ligne de code indique que le programe s'executera uniquement si on se trouve dans ce fichier
    main()
