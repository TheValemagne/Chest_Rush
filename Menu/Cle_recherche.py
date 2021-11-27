import tkinter

def cle (arg) :
    
    print("Touhce arg.keysym_num :",arg.keysym_num) # valeur de la touche tapée
    
Interface = tkinter.Tk()

Interface.bind("<KeyPress>",cle) # lorsque d’une touche est appuyée

Interface.mainloop() # lancement de la boucle
