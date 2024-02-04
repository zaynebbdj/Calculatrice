import tkinter as tk

# fonction d'évaluation
def evaluer () :
    try:
        resultat = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultat))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERREUR")


def ajouter(c):
    entry.insert(tk.END, c)

def effacer():
    entry.delete(0, tk.END)

# fenêtre principale
fenetre_principale = tk.Tk()
fenetre_principale.title("Calculatrice")

# entrées
entry = tk.Entry(fenetre_principale,width = 20, font=("Helvetica", 14))
entry.grid(row = 0, column = 0, columnspan = 4)

# tableau de boutons
boutons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('-', 4, 3)
]

etiquette = tk.Label(fenetre_principale, text="Bonjour, tkinter!")

for (content, ligne, colonne) in boutons:
    tk.Button(fenetre_principale,width = 5, height = 2,text = content,  command=lambda t=content: ajouter(t) if t != '=' else evaluer()).grid(row = ligne, column = colonne)

# bouton effacer
tk.Button(fenetre_principale,text = 'effacer', width = 5, height = 2, command = effacer).grid(row = 5, column = 0)



# boucle principale
fenetre_principale.mainloop()
