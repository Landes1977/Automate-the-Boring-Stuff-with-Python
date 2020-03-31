# Programmer: Matthew Landes
# Date:		  March 31, 2020
# Note:       Not perfect

import sys, re

text = sys.argv[1]

if len(sys.argv) > 2:
    regexStrip = re.compile(sys.argv[2])
    text2 = regexStrip.sub('', text)
else:
    text2 = text.strip()
  
print(text)
print(text2)