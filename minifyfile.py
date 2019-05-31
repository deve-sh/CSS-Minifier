'''
	Python Program to Take a filename and minify its CSS.
'''

# Importing sys Module for Command Line Arguments.

import sys

# Importing CSS Minifier

from cssminifier import cssminifier

# Function to take a filename as argument and then create a minified CSS file.

def minifyfile(filename):
	if(type(filename) is not str):
		print("\nInvalid type of filename.\n")
		exit()

	if(not filename.endswith("css")):
		raise Exception("\nNot a CSS File.\n")
		exit()

	namelist = filename.split('.')			# Splitting File Names

	file = ''
	minifiedfile = ''

	try:
		file = open(filename, "r")			# Opening the file.
	except:
		raise Exception("\nCould not open file.\n")
		exit()

	toedit = ''

	namelist[0] = namelist[0]+"-min"

	for namecomponent in namelist:
		toedit += (namecomponent + ".")		# Adding . at every run since there may be more than one seperator dot in the file name.

	try:
		minifiedfile = open(toedit,"w")		# Opening the file to write.
	except:
		raise Exception("\nCould not open file to read.\n")
		exit()

	try:
		string = file.read()

		minifiedcss = cssminifier(string)

		minifiedfile.write(minifiedcss)
	except:
		print("\nAn error occured during Minification.\n")

	minifiedfile.close()
	file.close()

	print("\nFile minified.\n")

# Now checking if there are enough Command Line Arguments.

if(len(sys.argv) < 2):
	raise Exception("\nNot enough arguments passed to the program. Usage : \npython minifyfile.py <file to minify>\n")
	exit()

minifyfile(sys.argv[1])