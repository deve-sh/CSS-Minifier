'''
	A Simple CSS Minifier.

	Author : Devesh Kumar.

	Process : 
	---------

	1. Get the CSS.
	2. Iterate over it character by character.
	3. Check if we are inside a comment. If yes, no need to add any characters inside the comment.
	4. If not, check if the character is a line break or an unnecessary whitespace. If yes, don't add it.
	5. If not, add the character to the minified css.
	6. Return the Minified CSS.
'''

# Importing Requirements

import re		# Regex Library

# Main Function to minify the CSS.

def cssminifier(css = ""):
	# Checking type of CSS
	if(type(css) is not str):
		print("\nInvalid Type CSS Passed.")
		exit()		# End execution

	# Required Variables

	minifiedcss = ''	# String that will be the Minified CSS.
	incomment = False	# Variable to keep track whether a comment is going on while iteration.
	spaceregex = "^[\s{}:;]$"	# Regex to check for unnecessary spaces.

	# Iterating over the CSS character by character.

	char = 0	# Iterator.

	while (char < len(css)):
		if(incomment == False):
			# If we are not inside a CSS comment.
			if(css[char] == '/'):
				if(char < len(css) - 1):
					if(css[char + 1] == '*'):
						# Start of a comment.
						incomment = True
						char += 1
						pass
			elif(css[char] == '\n'):
				# Line break.
				pass
			else:
				isspace = re.search("\s",css[char])
				nextisunnecessary = None
				previsunnecessary = None

				if(char < len(css) - 1 and char > 0):
					nextisunnecessary = re.search(spaceregex,css[char - 1])
					previsunnecessary = re.search(spaceregex, css[char + 1])

				if(isspace != None and (nextisunnecessary != None or previsunnecessary != None)):
					# The space is unnecessary
					pass
				else:
					minifiedcss += css[char]
		else:
			# If we are inside a comment.

			# Checking if the current character is a comment ender.

			if(css[char] == '*'):
				if(char < len(css) - 1):
					if(css[char + 1] == '/'):
						incomment = False	# No longer inside a comment.
						char += 1
						pass
			else:
				pass

		char += 1	# Keep incrementing character by character.

	# Now removing all the unnecessary semicolons from the string.

	minifiedcss = list(minifiedcss)

	char = 0

	while (char < len(minifiedcss)):
		if (char < len(minifiedcss) - 1):
			if(minifiedcss[char] == ';' and minifiedcss[char + 1] == '}'):
				minifiedcss[char] = ''	# Removing the block
		char += 1

	# Merging all the characters together.

	minifiedcss = ''.join(minifiedcss);

	# Returning the minifed CSS.

	return minifiedcss

''' 
# --------------------------------------------------------------
# Test Block : Remove the three single quotes above to run this.
# --------------------------------------------------------------

bigcss = """
/* This is a comment. */




body		{
	background : #ffffff;
	color :		blue;
    						}
.header{
	color : #fffff;
    }	
"""

print(cssminifier(bigcss))

'''