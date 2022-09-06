import collections
from functools import partial
import tkinter as tk
from tkinter.tix import TEXT
from turtle import back
import random

if __name__ == "__main__":
    # Créer la fenêtre de base
    root = tk.Tk()
    
    #fonction pour le button
    def foo():
        print("click")
        
    def log(texte):
        print(texte.get())    

    def couleur_aleatoire(label):
        couleur = "#"
        for i in range(0, 6):
            couleur += random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'])
        label.config(background=couleur) 
        
    # Ajouter un titre à la fenêtre 
    root.title("Ma première fenêtre tkinter")
    
    # Modieifier la taille (Largeur par hauteur)
    root.geometry("500x500")
    
    # Ajouter une étiquette de texte : 
    label = tk.Label(root, text="Hello world!", background="green", foreground="white", activebackground="yellow",
                     padx="25", pady="25", justify=tk.CENTER
                     )
    
    # Ajouter champs d'entrée (input)
    rep_champ = tk.StringVar(root)
    champ = tk.Entry(root, textvariable=rep_champ)
    label_champ = tk.Label(root, text="Entrez du texte")
    btn_champ = tk.Button(root, text="Afficher texte dans la console", command=partial(log, rep_champ))
    
    # Création d'un frame 
    frame = tk.Frame(root, bg='#aaa')
      
    
    # Ajouter un bouton 
    button = tk.Button(root, text="Cliquez sur moi", command=foo)
    button_2 = tk.Button(root, text="Changez la couleur du fond de texte", command=partial(couleur_aleatoire, label))
    
    #Afficher le champs 
    champ.grid(column=0, row=4)
    label_champ.grid(column=0, row=3)
    btn_champ.grid(column=1, row=3)
    
    # Affecter l'appuie sur une touche à un événement 
    root.bind('<')
    
    
    # Afficher le bouton
    button.grid(column=0, row=1)
    button_2.grid(column=1, row=0)
    
    # Affiche le label
    label.grid(column=0, row=0)
    
     # Lancer la boucle principale
    root.mainloop()
    
    
    
    
    # Notes sur les Widgets : 
    
    # un_widget = tk.UnWidget (root, autres = "")
    # un_widget.config(nom_param = "")
    # un_widget.Cget('nom_param')
    
    # Pour placer les widgets 
        # -> Pack 
        # -> Place(comme absolute dans CSS3)
        # -> grid(column = M, row = N)
    