import tkinter as tk
from tkinter import ttk

# fonction d'évaluation
def evaluer () :
    try:
        resultat = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultat))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERREUR")

def frame_convertion(type):
    try:

        convert_frame = tk.Toplevel(frame)
        convert_frame.title(f"Conversion - {type}")

        #bouton de convertion et champ d'entrée
        if type == 'Devise':
            champ1 = tk.Entry(convert_frame, width = 20, font=("Helvetica", 14))
            champ1.grid(row=0, column = 0, columnspan = 2)

            champ2 = tk.Entry(convert_frame, width = 20, font=("Helvetica", 14))
            champ2.grid(row=0, column = 2, columnspan = 2)

            tk.Button(convert_frame, text='convertion', width=10, height=2, command=lambda: convertion_devise(champ1, champ2)).grid(row=1, column=2)

            tk.Button(convert_frame, text='effacer', width=10, height=2, command=lambda: (effacer(champ1), effacer(champ2))).grid(row=1, column=0)


        if type == 'Temperature':
            champ = tk.Entry(convert_frame, width = 20, font=("Helvetica", 14))
            champ.grid(row=0, column = 0, columnspan = 4)

            tk.Button(convert_frame, text='convertion', width=10, height = 2, command=lambda: convertion_celsius(champ)).grid(row=1, column=1)

            tk.Button(convert_frame, text='effacer', width=10, height=2, command=lambda: effacer(champ)).grid(row=1, column=0)


        if type == 'Distance':

            # Créer une combobox avec les unites
            unites_francaise = ['Kilometres','Metres', 'Centimetres', 'Millimetres']
            unites_amer = ['Mile','Yard', 'Foot', 'Inch']

            combo_source = ttk.Combobox(convert_frame, values=unites_francaise)
            combo_source.grid(row=0, column=2, padx=5, pady=5)

            combo_dest = ttk.Combobox(convert_frame, values=unites_amer)
            combo_dest.grid(row=0, column=4, padx=5, pady=5)

            # champ
            champ1 = tk.Entry(convert_frame, width=20, font=("Helvetica", 14))
            champ1.grid(row=0, column=0)
            champ2= tk.Entry(convert_frame, width=20, font=("Helvetica", 14))
            champ2.grid(row=0, column=3)

            # Créer une étiquette pour afficher le résultat de la sélection
            label_result = tk.Label(convert_frame, text="Sélectionnez des unités")
            label_result.grid(row=1, column=0, padx=10, pady=10)

            tk.Button(convert_frame, text='convertion', width=10, height=2, command=lambda: convertion_distance(champ1, champ2, combo_source, combo_dest)).grid(row=1, column=3)

            tk.Button(convert_frame, text='effacer', width=10, height=2, command=lambda: (effacer(champ1), effacer(champ2))).grid(row=1, column=2)



    except Exception as e:
        champ.delete(0, tk.END)
        champ.insert(tk.END, "ERREUR")

def convertion_distance(champ1, champ2, box1, box2):
    try:
        if box2.get() == 'Mile':
            if box1.get() == 'Kilometres':
                champ2.insert(tk.END, float(champ1.get())* 0.621371)
            elif box1.get() == 'Metres':
                champ2.insert(tk.END, float(champ1.get())* 0.000621371)
            elif box1.get() == 'Centimetres':
                champ2.insert(tk.END, float(champ1.get())* 0.000621371 / 100)
            else:
                champ2.insert(tk.END, float(champ1.get())* 0.000621371 / 1000)
        if box2.get() == 'Yard':
            if box1.get() == 'Kilometres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61)
            elif box1.get() == 'Metres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 1000)
            elif box1.get() == 'Centimetres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 100000)
            else:
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 1000000)
        if box2.get() == 'Foot':
            if box1.get() == 'Kilometres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61)
            elif box1.get() == 'Metres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 1000)
            elif box1.get() == 'Centimetres':
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 100000)
            else:
                champ2.insert(tk.END, float(champ1.get())* 1093.61 / 1000000)
        if box2.get() == 'Inch':
            if box1.get() == 'Kilometres':
                champ2.insert(tk.END, float(champ1.get())* 3280.84)
            elif box1.get() == 'Metres':
                champ2.insert(tk.END, float(champ1.get())* 3280.84 / 1000)
            elif box1.get() == 'Centimetres':
                champ2.insert(tk.END, float(champ1.get())* 3280.84 / 100000)
            else:
                champ2.insert(tk.END, float(champ1.get())* 3280.84 / 1000000)

    except ValueError:
        champ1.delete(0, tk.END)
        champ1.insert(tk.END, 'RESULTAT')
        champ2.delete(0, tk.END)
        champ2.insert(tk.END, "ERREUR")


def convertion_devise(montant_entry, resultat_entry):
    try:
        resultat = float(montant_entry.get()) * float(resultat_entry.get())
        resultat_entry.delete(0, tk.END)
        resultat_entry.insert(tk.END, resultat)
    except ValueError:
        resultat_entry.delete(0, tk.END)
        resultat_entry.insert(tk.END, 'RESULTAT')
        montant_entry.delete(0, tk.END)
        montant_entry.insert(tk.END, "ERREUR")

def convertion_celsius(temp_entry):
    try:
        resultat = (float(temp_entry.get()) * 9/5) + 32
        temp_entry.delete(0, tk.END)
        temp_entry.insert(tk.END, resultat)
    except ValueError:
        temp_entry.delete(0, tk.END)
        temp_entry.insert(tk.END, "ERREUR")

def ajouter(c):
    entry.insert(tk.END, c)

def effacer(entr):
    entr.delete(0, tk.END)

# fenêtre principale
frame = tk.Tk()
frame.title("Calculatrice")

# entrées
entry = tk.Entry(frame,width = 20, font=("Helvetica", 14))
entry.grid(row = 0, column = 0, columnspan = 4)

# tableau de boutons
boutons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('/', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('-', 4, 3)
]


for (content, ligne, colonne) in boutons:
    tk.Button(frame,width = 5, height = 2,text = content,  command=lambda t=content: ajouter(t) if t != '=' else evaluer()).grid(row = ligne, column = colonne)

# bouton effacer
tk.Button(frame,text = 'effacer', width = 5, height = 2, command=lambda:  effacer(entry)).grid(row = 5, column = 3)

# bouton de convertion
convertions = [
        ('Devise',5, 0), ('Temperature', 5, 1), ('Distance', 5, 2)
    ]
for (content, ligne, colonne) in convertions:
    tk.Button(frame, width = 10, height = 3, text= content, command=lambda t=content: frame_convertion(t)).grid(row = ligne, column = colonne)


# boucle principale
frame.mainloop()
