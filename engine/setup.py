import subprocess
import os
import sys

def install_Git () :

    subprocess.Popen([r"Git.exe"])

def verify_Env (git_path) : 

	Environment = os.environ["Path"].split(";")

	Count = 0

	for path in Environment :

		if path.endswith("Git\\bin") :

			Count = 1

			break

	if Count == 0 :

		print("Besoin d'ajouter")

		os.environ["Path"] = os.environ["Path"] + ";" + git_path

