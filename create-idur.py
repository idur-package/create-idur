#!/usr/bin/python3
import os
import sys
from sys import exit


def main():
	print("Welcome to Create Idur!")
	if len(sys.argv) > 1:
		if sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("v0.8")
			exit()
		if sys.argv[1] == "-r" or sys.argv[1] == "--create-repo":
			create_repo()
			exit()
		if sys.argv[1] == "-p" or sys.argv[1] == "--create-package":
			create_idur()
			exit()
	see_help()
def see_help():
	print("""
create-idur <command>
Use:
    -r or --create-repo      Create file to detect repos
    -p or --create-package   Create a package (init)
    -v or --version          See version
    -h or --help             See Help
""")
	

def create_repo():
	it=True
	while it:
		Name = input("Repo Name: ")
		if " " in Name:
			print("Without space")
		elif "\n" in Name:
			print("no new lines")
		elif Name == "":
			print("write something")
		else:
			it=False
	it=True
	os.system("echo 'Name=\"" + Name + "\"' > standard.py")
def create_idur():
	Name=""
	Version=""
	it=True
	iti=True
	Depends=[]
	idurDepends=[]
	Conflict=[]
	License=""
	i=0

	while it:
		Name = input("Name of your program: ")
		if " " in Name:
			print("Without space")
		elif "\n" in Name:
			print("no new lines")
		elif Name == "":
			print("write something")
		else:
			it=False
	it=True

	while it:
		Version = input("Version of your program: ")
		if " " in Version:
			print("Without space")
		elif "\n" in Version:
			print("no new lines")
		elif Version == "":
			print("write something")
		else:
			it=False
	it=True
	i=0
	ask=input("do your program need apt depends? (y/n)")
	if ask == "y" or ask == "Y":
		while iti:
			while it:
				Depends.append(input("an apt depend (normal = name, recommend = rec/name, suggest = sug/name): "))
				if "\n" in Depends[i]:
					print("no new lines")
				elif Depends[i] == "":
					print("write something")
				else:
					it=False
			it=True
			ask=input("more? (y/n)")
			if ask == "y" or ask == "Y":
				iti=True
			else:
				iti=False
			i=i+1
		iti=True
	it=True

	i=0
	ask=input("do your program need idur depends? (y/n)")
	if ask == "y" or ask == "Y":
		while iti:
			while it:
				idurDepends.append(input("an idur depend (normal = name, recommend = rec/name, suggest = sug/name): "))
				if "\n" in idurDepends[i]:
					print("no new lines")
				elif idurDepends[i] == "":
					print("write something")
				else:
					it=False
			it=True
			ask=input("more? (y/n)")
			if ask == "y" or ask == "Y":
				iti=True
			else:
				iti=False
			i=i+1
		iti=True
	it=True
	i=0
	ask=input("conflict with other packages? (y/n)")
	if ask == "y" or ask == "Y":
		while iti:
			while it:
				Conflict.append(input("a conflict: "))
				if " " in Conflict[i]:
					print("Without space")
				elif "\n" in Conflict[i]:
					print("no new lines")
				elif Conflict[i] == "":
					print("write something")
				else:
					it=False
			it=True
			ask=input("more? (y/n)")
			if ask == "y" or ask == "Y":
				iti=True
			else:
				iti=False
			i=i+1
		iti=True
	it=True

	while it:
		ask=input("""architecture:

	all: one method to install with 64bits and 32bits
	x86_64: just 64bits
	i386: just 32bits
	both: one method to 64bits and other to 32bits

What is the architecture? 

		""")
		if ask == "all" :
			ARCH="all"
			it=False
		elif ask == "x86_64" :
			ARCH="x86_64"
			it=False
		elif ask == "i386" :
			ARCH="i386"
			it=False
		elif ask == "both" :
			ARCH="both"
			it=False
		else:
			print("error")
	it=True
		

	while it:
		ask=input("""Time:
		
	short - less than 30 seconds
	almost-medium - less than 1 minute
	medium - 1-2 minutes
	long - 3-10 minutes
	extra-long - +11minutes
	XXL - +1 hour

Aprox? 

		""")
		if ask == "short" :
			TIMEE="short"
			it=False
		elif ask == "almost-medium" :
			TIMEE="almost-medium"
			it=False
		elif ask == "medium" :
			TIMEE="medium"
			it=False
		elif ask == "long" :
			TIMEE="long"
			it=False
		elif ask == "XXL" :
			TIMEE="XXL"
			it=False
		else:
			print("error")
			TIMEE=""
	it=True


	ask=input("add License Link? (y/n)")
	if ask == "y" or ask == "Y":
		License = input("Link License: ")
	YourName=input("Your Name: ")
	YourEmail=input("Your Email: ")

	FILE="""Name=\"""" + Name + """\"
Version=\"""" + Version + """\"

Maintainer=\"""" + YourName + """\"
Contact=\"""" + YourEmail + """\"

Arch=\"""" + ARCH + """\"

Time=\"""" + TIMEE + """\"

"""
	
	if License != "":
		FILE+="""
License=\"""" + License + """\"
"""
	
	if len(Depends) != 0:
		FILE += "Depends=["
		for ii in range(len(Depends)):
			FILE += "\""
			FILE += Depends[ii]
			FILE += "\""
			if ii != len(Depends) -1:
				FILE += ", "
		FILE += "]\n"
		
	if len(idurDepends) != 0:
		FILE += 'idurDepends=["idur-pkg", "idur-exec", '
		for ii in range(len(idurDepends)):
			FILE += "\""
			FILE += idurDepends[ii]
			FILE += "\""
			if ii != len(idurDepends) -1:
				FILE += ", "
		FILE += "]\n"
	else:
		FILE += 'idurDepends=["idur-pkg", "idur-exec"]\n'
		
	if len(Conflict) != 0:
		FILE += "Conflict=[\"" + Name + "\", "
		for ii in range(len(Conflict)):
			FILE += "\""
			FILE += Conflict[ii]
			FILE += "\""
			if ii != len(Conflict) -1:
				FILE += ", "
		FILE += "]\n"
	else:
		FILE += "Conflict=[\"" + Name + "\"]"
		

	FILE += """
Description=\"\"\"

description here

\"\"\"
"""

	if ARCH == "all":
		FILE += """
Install=\"\"\"
# Install instructions here (bash)

# Temp Directory
idur-pkg tmp """ + Name + """
cd $(idur-pkg dp """ + Name + """)

# Download Files
idur-pkg download URL

# Copy Files
idur-pkg copy PATH NEWPATH

# Make Executable (chmod a+x)
idur-pkg exec PATH

# Remove Temp Directory
idur-pkg rm-tmp """ + Name + """

\"\"\"
"""
	if ARCH == "x86_64" or ARCH == "both":
		FILE += """
Install64=\"\"\"
# Install instructions here (bash)

# Temp Directory
idur-pkg tmp """ + Name + """
cd $(idur-pkg dp """ + Name + """)

# Download Files
idur-pkg download URL

# Copy Files
idur-pkg copy PATH NEWPATH

# Make Executable (chmod a+x)
idur-pkg exec PATH

# Remove Temp Directory
idur-pkg rm-tmp """ + Name + """

\"\"\"
"""
	if ARCH == "i386" or ARCH == "both":
		FILE += """
Install32=\"\"\"
# Install instructions here (bash)

# Temp Directory
idur-pkg tmp """ + Name + """
cd $(idur-pkg dp """ + Name + """)

# Download Files
idur-pkg download URL

# Copy Files
idur-pkg copy PATH NEWPATH

# Make Executable (chmod a+x)
idur-pkg exec PATH

# Remove Temp Directory
idur-pkg rm-tmp """ + Name + """

\"\"\"
"""
		


	FILE += """
Remove=\"\"\"
# Remove instructions here (bash)

# Remove Files and directories
idur-pkg rm PATHBIN
idur-pkg rm PATHFILES
idur-pkg rm PATHDESKTOP
idur-pkg rm PATHICON

\"\"\"
"""
	os.system("clear")
	print(FILE)
	ask = input("Good? (Y/n)")
	if ask == "Y" or ask == "y":
		print("Saved")
		TEMPFILE = open(Name + ".py", 'w')
		TEMPFILE.write(str(FILE))
	else:
		print("Not saved")

if __name__ == "__main__":
	main()
