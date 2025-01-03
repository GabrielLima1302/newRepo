import re
# \d means "a digit character", \d\d\d\d\d-\d\d\d\d is the regular expression for the correct phone number
"""
Matching Regex Objects
A Regex object’s search() method searches the string it is passed for any
matches to the regex. The search() method will return None if the regex pat-
tern is not found in the string. If the pattern is found, the search() method
returns a Match object. Match objects have a group() method that will return
the actual matched text from the searched string.
"""

phoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d') #the "r" is to make the string as a raw string, which does not escape characters "the \ doesn't disappear in \n or \d"
mo = phoneNumRegex.search('My number is 99502-8874')
print('Phone number found: ' + mo.group())

"""
Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each
step is fairly simple.

1. Import the regex module with import re.

2. Create a Regex object with the re.compile() function. (Remember to use a
raw string.)

3. Pass the string you want to search into the Regex object’s search() method.
This returns a Match object.

4. Call the Match object’s group() method to return a string of the actual
matched text.
"""








