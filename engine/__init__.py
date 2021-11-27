#!/usr/bin/python
# -*- coding: utf-8 -*-

Configuration = None # Configuration file for relative paths

def load () :

	"""Function called when module was imported and his configuration var was set."""

	vars()["importer"] = __import__(Configuration["ENGINE"]["Path"] + "." + "importer") # Codes importator

	for file in importer.os.listdir("./engine/") : # Listing all the files in the current directory

		if importer.os.path.isfile(Configuration["ENGINE"]["Path"] + "/" + file) and file.endswith(".py") and file != "__init__.py" : # If the file is a file and a python code and not the __init__ file

			vars()[file[:-3]] = __import__(Configuration["ENGINE"]["Path"] + "." + file[:-3]) # Setting the submodules as variables