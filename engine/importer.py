#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################################################
# Importations of the required modules to run the game
#########################################################################################

# Environnement gestion :

import os # System management
import subprocess # Cmd management
import platform # System informations
import shutil

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # Hide the pygame messages

# UI gestion :

import tkinter # Window system
from tkinter.messagebox import * # Message system
from tkinter.filedialog import * # Message system complement

# Sound and images gestion :

from PIL import Image, ImageTk # Image creation and manipulation
import pygame # Sound manager and tkinter complement

# Calculation :

import math # Gestion of shoots
import random # Gestion of randomisation

# Utils :

import time # Time system
import json # Storage system in json

# Parallel programmation

import socket # Socket
import threading # Multiple program management
import requests # Request management

# Github integration

try :

	import git as gt
	import git.repo.base as git

except :

	pass

#########################################################################################