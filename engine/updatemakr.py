import json
import os
import shutil

try :
	import git as gt
	import git.repo.base as git

except :

	pass

import requests

def check_Updates (url) :

	try :

		Version_File = requests.get(url)

		Online_Version = json.loads(Version_File.text)["Chest Rush"]["Version"]

		try :

			Current_Version = json.loads(open("./patchnote/curversion.json").read())["Chest Rush"]["Version"]

			if Current_Version != Online_Version :

				return True

			else :

				return False

		except :

			return True

	except :

		return None

def download (url,path) :

	try :

		git.Repo.clone_from(url,path)

	except :

		return False

def load_and_Organize_Tree (path) :

    Folder = os.listdir(path)

    for file in Folder :

    	if file.startswith("vers") :

    		Patch_Note = file

    		break

    Path = path + Patch_Note

    Patch_Note = open(Path).read()

    Data = json.loads(Patch_Note)

    shutil.move(Path,"./patchnote/" + "curversion.json")

    Folder = os.listdir("./patchnote/")

    for file in  Folder:

    	if file.endswith(".txt") :

    		break

    os.remove("./patchnote/" + file)

    shutil.move(path + Data["Chest Rush"]["Notes"],"./patchnote/")

    return Data["Chest Rush"]["Tree"]

def clean_Tmp (path) :

	os.system('rmdir /S /Q "{}"'.format(path))

def update (url,path,update = False) :

	try :

		download(url,path)

		Tree = load_and_Organize_Tree(path)

		for operation in Tree :

			if operation[0] == "UPDATE" and update == False:

				File = path + os.path.basename(__file__)

				File = open(File,"r")

				Data = File.readlines()

				Old_File = open(__file__,"w")

				Old_File.writelines(Data)

				Old_File.close()

				return True

			elif operation[0] == "REM" :

				if os.path.exists(operation[1]) :

					if os.path.isdir(operation[1]) :

						os.system('rmdir /S /Q "{}"'.format(operation[1]))

					else :

						File = operation[1]

						os.remove(File)

			elif operation[0] == "MOD" :

				File = path + operation[2]

				File = open(File,"r")

				Data = File.readlines()

				File = operation[1] + operation[2]

				Old_File = open(File,"w")

				Old_File.writelines(Data)

				Old_File.close()

			elif operation[0] == "CRE" :

				File_Extensions = [".txt",".json",".py",".png",".jpg",".ico"]

				Count = 0

				for extension in File_Extensions :

					if operation[1].endswith(extension) :

						Count += 1

						break

				if Count >= 1 :

					File = open(operation[1],"w")

					File.writelines(operation[2])

					File.close()

				else :

					os.mkdir(operation[1])

			elif operation[0] == "MOV" :

				Path = operation[1] + operation[3]

				shutil.move(Path,operation[2])

	except :

		return False

	clean_Tmp(path)

	return False


