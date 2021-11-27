from tkinter import *

class Menu:
	def __init__(self, root):

		self.root = root

		self.root.geometry("300x300")
		self.root.title('Option')

		#Background = Image.open("bg_game.jpg")
		#self.Font = ImageTk.PhotoImage(Background)
		#self.Background = self.Canvas.create_image((400, 400), image = self.Font) 

		text = Label(text = 'Menu')
		text.grid(padx = 10, pady = 20)

		self.Lunch = Button(self.root, text = 'Lancer', command = self.LunchGame, bg = 'green')
		self.Lunch.grid(padx = 30 ,pady = 10)
		self.optiongame = Button(self.root, text = 'Option', command = self.Option, bg = 'gray')
		self.optiongame.grid(padx = 30 ,pady = 10)
		self.quit = Button(self.root, text = 'Quitter', command = self.root.destroy, bg = 'red')
		self.quit.grid(padx = 30 ,pady = 10)



	def LunchGame(self):

	    LunchGameWindow = Tk()

	    LunchGameWindow.geometry("200x200")

	    LunchGameWindow.title("Jeu")

	def Option(self):

		Keys = {}
		Key_Binding = {}

		def change_Focus (self,args) :

			self.Current_Window = int(args.widget)

		def attribute_Key(self,args) :

			for entry[0] in self.Keys :

				if self.Current_Window == int(entry[0]) :

					entry[0].est(args.Keysym_num)

					open("salut").write()

					entry[0].itemconfig(state = "disabled")

					break

		def change_State (self,args) : 
			
			for entry[0] in self.Keys : 
				
				if self.Current_Window == int(entry[0]) :

					entry[0].itemconfig(state = "normal")

					break

		Value = StringVar()
		Value1 = StringVar()
		Value2 = StringVar()
		Value3 = StringVar()
		for key in Key_Binding : 

			Value.set(key) <="up"

			State = "normal"

			Entry_Iter = Entry(textvariable = Value, state = state)

			self.Key_Binding[key] = (State,Value,Entry_Iter)

		self.root.bind("<KeyRelease>",attribute_Key)
		self.root.bind("<Enter>",change_Focus)
		self.root.bind("<Double-Button-1>",change_State)


		Current_Window = Tk()

		Current_Window.geometry("250x150")

		Current_Window.title("Option")

		title = Label(Current_Window, text = 'Option de clavier')
		title.grid(row = 0, column = 0)

		up = Label(Current_Window, text="up")
		up.grid(row = 1, column = 0)

		up_entry = Entry(Current_Window, textvariable = Value)
		up_entry.grid(row = 1, column = 1) 

		down = Label(Current_Window, text="Down")
		down.grid(row = 2, column = 0)

		down_entry = Entry(Current_Window, textvariable = Value1)
		down_entry.grid(row = 2, column = 1)

		left=Label(Current_Window, text="Left")
		left.grid(row = 3, column = 0)

		left_entry = Entry(Current_Window, textvariable = Value2)
		left_entry.grid(row = 3, column = 1)

		right = Label(Current_Window, text="right")
		right.grid(row = 4, column = 0)

		right_entry = Entry(Current_Window, textvariable = Value3)
		right_entry.grid(row = 4, column = 1)

		Close = Button(Current_Window, text = 'Close', bg = 'red', command = Current_Window.destroy)
		Close.grid(padx = 40, pady = 10)


root = Tk()
Menu(root)
root.mainloop()