#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################################################
# Importations of the required modules to run the launcher
#########################################################################################

import configparser # Ini file reader for paths management system

#########################################################################################

Configuration = configparser.ConfigParser() # Configuration of the ini reader
Configuration.read("./config/configuration.ini") # Reading paths from the configuration file

###############################################
# Engine importation
###############################################

engine = __import__(Configuration["ENGINE"]["Path"]) # Importing engine folder with the path from the configuration file
engine.Configuration = Configuration # Passing required variables to the engine module
engine.load() # Loading all the files with the path set by the configuration file

importer = engine.importer # Setup the importer

###############################################
# Session informations for the log file
###############################################

Current_Version_Data = importer.json.loads(open(Configuration["VERSION"]["Path"] + "curversion.json").read()) # Reading build data from version file
Session_File = Configuration["REGISTRY"]["Path"] + "session_" + importer.time.strftime("%H-%M&%d-%m-%Y") + ".txt" # Creating the session file name
Date = importer.time.strftime("the %d-%m-%Y at %Hh%M") # Creating the date format to include in the session file

logger = engine.logger # Setup the logger
logger.Session_Infos = Session_File, Date, Current_Version_Data["Chest Rush"]["Build"]

Running = True

###############################################

class Launcher :

	# Debug

	Debug = False # Debug for developer

	######################################

	# UI gestion

	Launch_Icon = 640,640
	Padding_Bar = 160,100,120
	Fill_Interval = Padding_Bar[0]/100
	Progression = 0
	Glow = False

    ######################################

    # Ressources for the game

	Web_Storage = importer.json.loads(open("./config/webaccess.json").read())	
	Log = importer.time.strftime("%H-%M&%d-%m-%Y"), importer.time.strftime("the %d-%m-%Y at %Hh%M") # Time when the game was launched

	def __init__ (self,Master) :

		self.Master = Master # Attribution of master to the entire class

		logger.log_Operation("Master __init__() ran with success", op_time = importer.time.strftime("[%X] : "))

		importer.pygame.mixer.init()

		logger.log_Operation("pygame __init__() ran with success",op_time = importer.time.strftime("[%X] : "))

        ########################################################################################

        # UI gestion

		logger.log_Operation("getting coordinates for alignation", op_time = importer.time.strftime("[%X] : "))

		Coords = self.align_Window(self.Launch_Icon) # Get the coordinates for the center of the screen

		logger.log_Operation("coordinates for window alignation set", op_time = importer.time.strftime("[%X] : "))

		Master.geometry("%dx%d+%d+%d" % (self.Launch_Icon[0], self.Launch_Icon[1], Coords[0], Coords[1])) # Align the window

		logger.log_Operation("Master alignated on screen", op_time = importer.time.strftime("[%X] : "))

		Master.overrideredirect(True) # Delete tkinter default UI

		logger.log_Operation("Master overrided with success", op_time = importer.time.strftime("[%X] : "))

		Master.wm_attributes("-topmost",True) # Obligate the UI to be in the first position of the screen

		logger.log_Operation("Master topmost activated", op_time = importer.time.strftime("[%X] : "))

		Master.wm_attributes("-transparentcolor","#666a6c") # Set the black color to transparent

		logger.log_Operation("Master transparentcolor assignated", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("setting icon file", op_time = importer.time.strftime("[%X] : "))

		Master.iconbitmap(Configuration["STORAGE"]["Path"] + "icons/" + Configuration["GAME"]["Ico"])

		logger.log_Operation("icon file set with success", op_time = importer.time.strftime("[%X] : "))

		########################################################################################

		# Canvas gestion

		logger.log_Operation("creating canvas", op_time = importer.time.strftime("[%X] : "))

		self.Font = importer.tkinter.Canvas(Master,bg = "#666a6c",
		                            			width = self.Launch_Icon[0],
		                            			height = self.Launch_Icon[1],
		                            			highlightthickness=0) # Canva for the auth window

		logger.log_Operation("canvas created with success", op_time = importer.time.strftime("[%X] : "))

		self.Font.pack() # Placement of the canva

		logger.log_Operation("canvas placed on Master with success", op_time = importer.time.strftime("[%X] : "))

		self.Icon = importer.ImageTk.PhotoImage(file = Configuration["STORAGE"]["Path"] + "icons/" + Configuration["GAME"]["Splash"]) # Image to display

		logger.log_Operation("splash screen one image created with success", op_time = importer.time.strftime("[%X] : "))

		self.Team = importer.ImageTk.PhotoImage(file = Configuration["STORAGE"]["Path"] + "/icons/" + Configuration["GAME"]["End_Splash"]) # Image to display

		logger.log_Operation("splash screen two image created with success", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("creating pygame.mixer", op_time = importer.time.strftime("[%X] : "))

		Splash_Sound = importer.pygame.mixer.Sound(Configuration["STORAGE"]["Path"] + "sounds/spray.wav")

		logger.log_Operation("pygame.mixer created with success", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("starting splash sound", op_time = importer.time.strftime("[%X] : "))

		Splash_Sound.play()

		logger.log_Operation("splash sound playing with success", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("launching splash screen", op_time = importer.time.strftime("[%X] : "))

		Master.after(1500,
						self.splash_Screen)

	def align_Window (self,window_size) :   # Center windows and object on the screen

		logger.log_Operation("align_Window() ran with success", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("getting screen sizes", op_time = importer.time.strftime("[%X] : "))

		Screen_width = self.Master.winfo_screenwidth() # Get the width of the screen
		Screen_height = self.Master.winfo_screenheight() # Get the height of the screen

		logger.log_Operation("screen sizes acquired with success", op_time = importer.time.strftime("[%X] : "))

		X = (Screen_width/2) - (window_size[0]/2) # Coordinate x for the alignation

		Y = (Screen_height/2) - (window_size[1]/2) # Coordinate y for the coordination

		logger.log_Operation("center coordinates calculated", op_time = importer.time.strftime("[%X] : "))

		return [X, Y]

	def ask_Update (self) :

		Answer = importer.askyesno("UPDATE CLIENT","An update is available, do you want to install it?")

		if Answer :

			Need_Relaunch = engine.updatemakr.update(self.Web_Storage["Access"]["Download"],"./temp/")

			if Need_Relaunch :

				Need_Relaunch = engine.updatemakr.update(self.Web_Storage["Access"]["Download"],"./temp/",update = True)

		else :

			pass

	def check_Game_Version (self,display = True,count = 0) :

		self.update_Status("CHECKING GAME VERSION")

		logger.log_Operation("check_Game_Version() ran with success", op_time = importer.time.strftime("[%X] : "))

		logger.log_Operation("verifying game version", op_time = importer.time.strftime("[%X] : "))

		self.update_Status("CONNECTING TO DATABASE")

		Need_Update = engine.updatemakr.check_Updates(self.Web_Storage["Access"]["Version"])

		logger.log_Operation("game version and response acquired with success", op_time = importer.time.strftime("[%X] : "))

		if Need_Update == True :

			self.update_Status("NEW VERSION AVAILABLE")

			logger.log_Operation("client is running on an old version", op_time = importer.time.strftime("[%X] : "))

			logger.log_Operation("asking update to user", op_time = importer.time.strftime("[%X] : "))

			self.ask_Update()

		elif Need_Update == None :

			self.update_Status("CLIENT OFFLINE")

			logger.log_Operation("response not acquired, client probably offline", op_time = importer.time.strftime("[%X] : "))

			if count != 0 :

				if count <= 5 :

					logger.log_Operation("retrying to establish a connection", op_time = importer.time.strftime("[%X] : "))

					count += 1

					self.Master.after(2000,
										self.check_Game_Version,False,count)

					return

				else :

					logger.log_Operation("reconnection tried but failed, launching in stand-alone mode", op_time = importer.time.strftime("[%X] : "))

					logger.log_Operation("displaying alert to user", op_time = importer.time.strftime("[%X] : "))

					importer.showinfo("PROBLEM", "It seems like we cannot establish any connection to the server, the game will be launched in stand-alone mode.")

					logger.log_Operation("alert displayed with success", op_time = importer.time.strftime("[%X] : "))

					return

			logger.log_Operation("asking retry to user", op_time = importer.time.strftime("[%X] : "))

			Answer = importer.askyesno("CLIENT OFFLINE","The client is actually offline do you want to retry to connect ?")

			if Answer :

				logger.log_Operation("retry connection", op_time = importer.time.strftime("[%X] : "))

				logger.log_Operation("displaying alert to user", op_time = importer.time.strftime("[%X] : "))

				importer.showinfo("AWAIT", "The client will retry to connect several times.")

				logger.log_Operation("alert displayed with success", op_time = importer.time.strftime("[%X] : "))

				logger.log_Operation("reconnection count", op_time = importer.time.strftime("[%X] : "))

				self.Master.after(5000,
									self.check_Game_Version,False,1)

			else :

				logger.log_Operation("launching game with old version, stand-alone mode activated", op_time = importer.time.strftime("[%X] : "))

				importer.showinfo("CONTINUE", "The client will be launched in stand-alone mode.")

		else :

			self.update_Status("CLIENT UP TO DATE")

	def update_Status (self,status) :

		self.Font.itemconfig(self.Status,text = status)

	def update_Glowing (self) :

		"""Function used to make the progress bar glowing"""

		try :

			if self.Glow : # If True

				Color = "#C7CF00" # Color of the progress bar

				self.Glow = False # Set to false

			else :

				Color = "#FEF86C" # Color of the progress bar

				self.Glow = True # Set to true

			self.Font.itemconfig(self.Bar,fill = Color) # Configuring the color of the bar

			try : 

				if Running == True :

					self.Master.after(300,
										self.update_Glowing) # Re-updating after x ms

			except :

				return

		except :

			return

	def update_Loading_Bar (self,*args) :

		try :

			self.Font.delete(self.Bar)
			self.Font.delete(self.Status)

		except :

			pass

		self.Bar = self.Font.create_rectangle(self.Launch_Icon[0]/2 - self.Padding_Bar[0],
												self.Launch_Icon[1]/2 + self.Padding_Bar[1],
												self.Launch_Icon[0]/2 + self.Fill_Interval * self.Progression,
												self.Launch_Icon[1]/2 + self.Padding_Bar[2],
												fill = "red",
												width = 3,
												outline = "black")

		self.Status = self.Font.create_text(self.Launch_Icon[0]/2,
												self.Launch_Icon[1]/2 + (self.Padding_Bar[1] + self.Padding_Bar[2])/2,
												font = ("Open Sans",12),
												fill = "#202020",
												text = "LOADING ...") # Label displaying the name of the game

		try :
			
			self.update_Glowing()

		except :

			pass

		if self.Progression <= 100 :

			self.Progression += 5

			self.Master.after(500,
                                                  self.update_Loading_Bar)

		else :

                        print("DEAD")
                        self.Running = False
                        self.Master.destroy()
                        Root.quit()

	def splash_Screen (self) :

		"""Function used to generate the splash screen animation"""

		logger.log_Operation("splash_Screen() ran with success", op_time = importer.time.strftime("[%X] : ")) # Logging operation

		def splash (x,y,image) :

			"""Function used to create the splash image"""

			logger.log_Operation("create_Image() ran with success", op_time = importer.time.strftime("[%X] : ")) # Logging operation

			try : # Trying to do the following lines

				self.Font.delete(self.Splash) # Deleting old splash image

				logger.log_Operation("old splash screen image deleted", op_time = importer.time.strftime("[%X] : ")) # Logging operation

				self.Font.create_image(self.Launch_Icon[0]/2, self.Launch_Icon[1]/2, image = image)

				self.Font.image = image

				logger.log_Operation("new splash screen image created with success", op_time = importer.time.strftime("[%X] : "))

				logger.log_Operation("creating loading bar", op_time = importer.time.strftime("[%X] : "))

				self.Font.create_rectangle(self.Launch_Icon[0]/2 - self.Padding_Bar[0],
											self.Launch_Icon[1]/2 + self.Padding_Bar[1],
											self.Launch_Icon[0]/2 + self.Padding_Bar[0],
											self.Launch_Icon[1]/2 + self.Padding_Bar[2],
											fill = "white",
											width = 3,
											outline = "black")

				self.update_Loading_Bar()

				logger.log_Operation("loading bar created with success", op_time = importer.time.strftime("[%X] : "))

				logger.log_Operation("fetching cache data", op_time = importer.time.strftime("[%X] : "))

				Cache = importer.os.listdir(Configuration["REGISTRY"]["Path"])

				logger.log_Operation("data fetched from cache", op_time = importer.time.strftime("[%X] : "))

				if len(Cache) >= 5 :

					logger.log_Operation("too much data in cache", op_time = importer.time.strftime("[%X] : "))

					logger.log_Operation("asking deletion to user", op_time = importer.time.strftime("[%X] : "))

					Answer = importer.askyesno("CACHE TOO BIG","It seems like the log folder is full (loss of accuracy, calculations and memory gestion), do you want to clean it ?")

					if Answer :

						logger.log_Operation("processing old data deletion", op_time = importer.time.strftime("[%X] : "))

						for file in Cache :

							if Configuration["REGISTRY"]["Path"] + file  != Session_File :

								importer.os.remove(Configuration["REGISTRY"]["Path"] + file)

						logger.log_Operation("cache cleaned with success", op_time = importer.time.strftime("[%X] : "))

				logger.log_Operation("launching version verification process", op_time = importer.time.strftime("[%X] : "))

				self.Master.after(500,
									self.check_Game_Version)

			except:
				
				logger.log_Operation("creating first splash screen image", op_time = importer.time.strftime("[%X] : "))

				self.Splash = self.Font.create_image(self.Launch_Icon[0]/2, self.Launch_Icon[1]/2, image = image)

				logger.log_Operation("first splash screen created with success", op_time = importer.time.strftime("[%X] : "))

				self.Master.after(1600,
									splash,self.Launch_Icon[0]/2, self.Launch_Icon[1]/2, self.Team)

		logger.log_Operation("creating splash screen image", op_time = importer.time.strftime("[%X] : "))

		splash(self.Launch_Icon[0]/2, self.Launch_Icon[1]/2, self.Icon)

		logger.log_Operation("splash screen created with success", op_time = importer.time.strftime("[%X] : "))

Root = importer.tkinter.Tk()

Launcher(Root)

Root.mainloop()

engine.logger.log_Operation("initialisation succeed", op_time = importer.time.strftime("[%X] : ")) # Logging operation

Bit_Version = importer.platform.architecture() # Getting bit version of the running client (x86,x64)

engine.logger.log_Operation("platform identified", op_time = importer.time.strftime("[%X] : ")) # Logging operation

if Bit_Version[0] == "64bit" : # 64 bit versions

	engine.logger.log_Operation("client running on a x64 structure", op_time = importer.time.strftime("[%X] : ")) # Logging operation

	import game_x64 # Importation of the x64 version of the game

	###############################################
	# Passing informations to the game module
	###############################################

	game_x64.Configuration = Configuration # Passing the configuration params to the game
	game_x64.engine = engine # Passing the engine param to the game
	game_x64.Session_File = Session_File # Passing the session informations to the game
	game_x64.Current_Version_Data = Current_Version_Data # Passing the actual build infos to the games

	###############################################

	game_x64.init_Game() # Launching the launcher when all variables were passed

else : # 32 bit version

	engine.logger.log_Operation("client running on a x32 structure", op_time = importer.time.strftime("[%X] : ")) # Logging operation

	import game_x32 # Importation of the x32 version of the game

	####################d###########################
	# Passing informations to the game module
	###############################################

	game_x32.Configuration = Configuration # Passing the configuration params to the game
	game_x32.engine = engine # Passing the engine param to the game
	game_x32.Session_File = Session_File # Passing the session informations to the game
	game_x32.Current_Version_Data = Current_Version_Data # Passing the actual build infos to the game

	###############################################

	game_x32.init_Game() # Launching the launcher when all variables were passed
