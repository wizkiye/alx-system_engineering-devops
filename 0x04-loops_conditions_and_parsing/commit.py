import os
import subprocess

for path, subdirs, files in os.walk("./"):
	if not ".git" in path:
	    for name in files:
	        if name != "commit.py" and name != "main.py":
	            subprocess.run(['git', 'add', os.path.join(path, name)])
	            subprocess.run(['git', 'commit', '-m', name])
