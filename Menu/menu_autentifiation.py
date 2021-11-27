from tkinter import *

class Menu:
	def __init__(self, root):
		nom_entry_variable = StringVar()
		mdp_entry_variable = StringVar()

		self.root = root

		self.root.geometry("250x200")
		self.root.title('Menu d’identification')

		nom = Label(text = 'Nom d’utilisateur')
		nom.grid(padx = 65, pady = 2)
		nomentry = Entry(textvariable = nom_entry_variable)
		nomentry.grid(padx = 65, pady = 0)

		mdp = Label(text = 'Mot de passe')
		mdp.grid(padx = 65, pady = 0)
		mdpentry = Entry(textvariable = mdp_entry_variable)
		mdpentry.grid(padx = 65, pady = 0)

		self.Lunch = Button(self.root, text = 'Lancer', bg = 'green',command = self.root.destroy)
		self.Lunch.grid(padx = 0, pady = 15)
		self.quit = Button(self.root, text = 'Quitter', command = self.root.destroy, bg = 'red')
		self.quit.grid(padx = 30, pady = 0)


root = Tk()
Menu(root)
root.mainloop()