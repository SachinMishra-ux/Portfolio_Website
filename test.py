import re

l='sachin19566@gmail.com'

match= re.match("[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*",l)
#print(type(match))
if match:
    print(match.group(0))