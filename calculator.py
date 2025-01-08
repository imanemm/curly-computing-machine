#Simple calculator
#Décembre 2024

import tkinter as tk
from tkinter import ttk

#Définiton des fonctions importantes
def click_button(valeur):
    '''Traite les clics de bouton pour ajouter des nombres/opérateurs au widget d'entrée.'''
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(valeur))

def effacer():
    '''Efface le widget d'entrée.'''
    entry.delete(0, tk.END)

def calculate():
    '''Évaluer l'expression mathématique.'''
    try:
        resultat = eval(entry.get()) #Évalue l'expression en sécurité
        entry.delete(0, tk.END)
        entry.insert(0, str(resultat))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

#Création de la fenêtre principale
root = tk.Tk()
root.title("Simple Calculator")

#Personalisation de la calculatrice
root.geometry("300x300")
root.configure(bg="lightblue")


#Entry Widget for Input and Output
entry = tk.Entry(root,width=25, font=("Arial", 16), borderwidth=5)
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=10)

#Définition du style des buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.map(
    "TButton",
    background=[("active", "#E5D9B2")],
    foreground=[("active", "#FFFFFF")],
)
#Définition des buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        button = ttk.Button(
            root, text=text, style="TButton", command=calculate
        )
    elif text == "C":
        button = ttk.Button(
            root, text=text, style="TButton", command=effacer
        )
    else:
        button = ttk.Button(
            root, text=text, style="TButton", command=lambda t=text: click_button(t)
        )
    button.grid(row=row, column=col, padx=5, pady=5)

#Exécutation de l'application
root.mainloop()