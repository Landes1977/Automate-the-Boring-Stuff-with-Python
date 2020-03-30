# Programmer: Matthew Landes
# Date:		  March 29, 2020

import re

print('Enter a password:')
password = input()

passwordRegex = re.compile(r'''(
	[a-z]+		# at least 1 lowercase
	[A-Z]+		# at least 1 uppercase
	[0-9]+		# at least
	)''', re.VERBOSE)
	
if (len(password) > 7) & (passwordRegex.search(password) != ''):
	print('Password accepted')
else:
	print('Weak password')