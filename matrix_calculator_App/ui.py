import tkinter as tk
# Import du module Tkinter pour créer l'interface graphique de base

from tkinter import ttk, messagebox
# Import des widgets modernes (ttk) et des boîtes de dialogue (messagebox)

import numpy as np
# Import de NumPy pour les opérations matricielles

from matrix_ops import (
    add, subtract, multiply, divide,
    determinant, inverse, transpose, scalar_multiply
)
# Import des fonctions de calcul matriciel depuis le module matrix_ops

from validators import parse_matrix
# Import de la fonction de validation et de parsing des matrices

from visualization import visualize_matrix
# Import de la fonction permettant de visualiser une matrice sous forme graphique
# =======================
# PALETTE DE COULEURS
# =======================
BG_MAIN = "#1e1e2e"      # Couleur principale du fond de la fenêtre
BG_FRAME = "#2a2a3c"     # Couleur des cadres et cartes
BG_INPUT = "#24283b"     # Couleur des champs de saisie
BG_RESULT = "#16161e"    # Couleur de la zone de résultat

FG_TEXT = "#eaeaf0"       # Couleur principale du texte
FG_ACCENT = "#7aa2f7"     # Couleur accentuée pour les boutons
FG_SUCCESS = "#9ece6a"    # Couleur du texte de résultat réussi
FG_ERROR = "#f7768e"      # Couleur pour les erreurs ou validation échouée



class MatrixCalculatorUI:
    """
    Classe représentant l'interface graphique du calculateur matriciel
    en Dark Mode, moderne et élégant.
    """

    def __init__(self, root: tk.Tk) -> None:
        # Constructeur : initialisation de la fenêtre principale et de l'UI

        self.root = root
        # Stocke la référence à la fenêtre Tk principale

        self.root.title("Calculatrice Matricielle du GROUPE 2")
        # Définit le titre de la fenêtre

        self.root.geometry("950x650")
        # Définit la taille initiale de la fenêtre

        self.root.configure(bg=BG_MAIN)
        # Applique la couleur de fond principale (dark mode)

        self._configure_style()
        # Appelle la méthode pour configurer les styles ttk (boutons, labels, cadres)

        self._build_ui()
    # Appelle la méthode pour construire tous les composants de l'interface


        # =======================
    # CONFIGURATION DU STYLE
    # =======================
    def _configure_style(self) -> None:
        # Configure les styles des widgets ttk pour le dark mode

        style = ttk.Style()
        style.theme_use("clam")
        # Utilisation d'un thème ttk compatible avec la personnalisation

        style.configure("TFrame", background=BG_MAIN)
        # Style par défaut des frames

        style.configure("Card.TFrame", background=BG_FRAME)
        # Style spécifique pour les cartes ou sections encadrées

        style.configure(
            "Title.TLabel",
            background=BG_MAIN,
            foreground=FG_TEXT,
            font=("Segoe UI", 18, "bold")
        )
        # Style du titre principal

        style.configure(
            "TLabel",
            background=BG_FRAME,
            foreground=FG_TEXT,
            font=("Segoe UI", 10)
        )
        # Style général pour les labels

        style.configure(
            "Accent.TButton",
            background=FG_ACCENT,
            foreground="black",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )
        # Style des boutons avec couleur accentuée

        style.map(
            "Accent.TButton",
            background=[("active", "#89b4fa")]
        )
        # Changement de couleur du bouton au survol ou clic


        # =======================
    # CONSTRUCTION UI
    # =======================
    def _build_ui(self) -> None:
        # Construction de tous les composants graphiques

        container = ttk.Frame(self.root)
        container.pack(fill="both", expand=True, padx=20, pady=20)
        # Conteneur principal centré, avec padding et responsive

        # ===== TITRE =====
        ttk.Label(
            container,
            text="Calculatrice Matricielle",
            style="Title.TLabel"
        ).pack(pady=(0, 20))
        # Label du titre principal avec espacement vertical

        ttk.Label(
            container,
            text="Proposé par les membres du GROUPE 2: NGOUNGOURE NJIKAM Nadia & MBASSI PIUS B",
            style="Subtitle.TLabel"
        ).pack(pady=(0, 10))
        # Label sous-titre présentant les auteurs



        # ===== MATRICES =====
        matrices_frame = ttk.Frame(container)
        matrices_frame.pack(fill="x")
        # Frame contenant les zones de saisie des matrices A et B

        self.text_a = self._create_matrix_card(matrices_frame, "Matrice A")
        self.text_b = self._create_matrix_card(matrices_frame, "Matrice B")
        # Création des cartes de saisie pour A et B via une méthode dédiée

        # ===== SCALAIRE =====
        scalar_frame = ttk.Frame(container, style="Card.TFrame")
        scalar_frame.pack(fill="x", pady=15)
        # Frame pour l'entrée scalaire

        ttk.Label(scalar_frame, text="Scalaire").pack(side="left", padx=10)
        # Label pour le champ scalaire

        self.scalar_entry = ttk.Entry(
            scalar_frame,
            width=10,
            font=("Consolas", 11)
        )
        self.scalar_entry.pack(side="left")
        self.scalar_entry.configure(background=BG_INPUT, foreground=BG_FRAME)
        # Champ d'entrée du scalaire avec couleur et police définies

        # ===== BOUTONS =====
        buttons_frame = ttk.Frame(container, style="Card.TFrame")
        buttons_frame.pack(fill="x", pady=15)
        # Frame pour tous les boutons d'opération

        buttons = [
            ("A + B", lambda: self.binary_op(add)),
            ("A - B", lambda: self.binary_op(subtract)),
            ("A × B", lambda: self.binary_op(multiply)),
            ("A ÷ B", lambda: self.binary_op(divide)),
            ("det(A)", self.det_a),
            ("inv(A)", self.inv_a),
            ("Aᵀ", self.trans_a),
            ("Scalaire × A", self.scalar_a),
            ("Visualiser A", self.visualize_a),
        ]
        # Liste des boutons et actions associées (opérations matricielles)

        for i, (label, cmd) in enumerate(buttons):
            ttk.Button(
                buttons_frame,
                text=label,
                style="Accent.TButton",
                command=cmd
            ).grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")
             # Placement des boutons en grille 3 colonnes avec espacement et responsive

        # ===== RÉSULTAT =====
        result_frame = ttk.Frame(container, style="Card.TFrame")
        result_frame.pack(fill="both", expand=True)
        # Frame pour la zone de résultat

        ttk.Label(result_frame, text="Résultat").pack(anchor="w", padx=10, pady=5)
        # Label indiquant la zone de résultat

        self.result = tk.Text(
            result_frame,
            height=8,
            font=("Consolas", 11),
            bg=BG_RESULT,
            fg=FG_SUCCESS,
            insertbackground=FG_TEXT,
            relief="flat"
        )
        self.result.pack(fill="both", expand=True, padx=10, pady=10)
        # Zone texte pour afficher les résultats des opérations

        # =======================
    # COMPOSANTS MATRICES
    # =======================
    def _create_matrix_card(self, parent, title: str) -> tk.Text:
        # Méthode pour créer un "card" contenant un label et un champ texte

        card = ttk.Frame(parent, style="Card.TFrame")
        card.pack(side="left", expand=True, fill="both", padx=10)
        # Frame individuelle pour une matrice

        ttk.Label(card, text=title).pack(anchor="w", padx=10, pady=5)
        # Label indiquant le nom de la matrice

        text = tk.Text(
            card,
            height=8,
            font=("Consolas", 11),
            bg=BG_INPUT,
            fg=FG_TEXT,
            insertbackground=FG_TEXT,
            relief="flat"
        )
        text.pack(fill="both", expand=True, padx=10, pady=10)
        # Champ texte pour saisir la matrice

        return text
        # Retourne le widget texte pour interaction dans d'autres méthodes


        # =======================
    # VALIDATION AVANCÉE
    # =======================
    def _get_matrix(self, widget: tk.Text) -> np.ndarray:
        # Récupère une matrice depuis un champ texte et valide le format

        try:
            widget.configure(bg=BG_INPUT)
            # Reset couleur du champ en cas d'erreur précédente
            return parse_matrix(widget.get("1.0", tk.END))
            # Parse la saisie en matrice NumPy
        except Exception:
            widget.configure(bg=FG_ERROR)
            # Indique visuellement une erreur
            raise ValueError("Format de matrice invalide")


    def _display(self, output) -> None:
        # Affiche le résultat dans la zone texte
        self.result.delete("1.0", tk.END)
        self.result.configure(fg=FG_SUCCESS)

        if isinstance(output, np.ndarray):
            for row in output:
                self.result.insert(tk.END, " ".join(map(str, row)) + "\n")
                # Affiche chaque ligne de la matrice
        else:
            self.result.insert(tk.END, str(output))
            # Affiche un résultat scalaire

    # =======================
    # ACTIONS SUR LES MATRICES
    # =======================
    def binary_op(self, operation) -> None:
        # Effectue une opération binaire entre A et B

        try:
            a = self._get_matrix(self.text_a)
            b = self._get_matrix(self.text_b)
            self._display(operation(a, b))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
            # Affiche un message d'erreur si l'opération échoue

    def det_a(self) -> None:
        try:
            a = self._get_matrix(self.text_a)
            self._display(determinant(a))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
         # Calcul et affichage du déterminant de A

    def inv_a(self) -> None:
        try:
            a = self._get_matrix(self.text_a)
            self._display(inverse(a))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        # Calcul et affichage de l'inverse de A

    def trans_a(self) -> None:
        try:
            a = self._get_matrix(self.text_a)
            self._display(transpose(a))
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        # Calcul et affichage de la transposée de A

    def scalar_a(self) -> None:
        try:
            a = self._get_matrix(self.text_a)
            scalar = float(self.scalar_entry.get())
            self._display(scalar_multiply(a, scalar))
        except Exception:
            self.scalar_entry.configure(foreground=FG_ERROR)
            messagebox.showerror("Erreur", "Scalaire invalide")
        # Multiplication d'A par un scalaire

    def visualize_a(self) -> None:
        try:
            a = self._get_matrix(self.text_a)
            visualize_matrix(a, "Matrice A")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
        # Affiche la matrice A sous forme graphique (heatmap)
