import re
#{} are used to find a pattern that repeats many times in sequence

"""pattern = re.compile(r'(hello){3}')
text = 'hello0o hello hellohello, hellohellohello'
findtext = pattern.search(text)
print("Your text that was repeated 3 times is: ", findtext.group())"""

#instead of one number, you can specify a range by writing a minimum and a maximum

pattern = re.compile(r'(hello){2,4}')
text = 'hello hellohello , hellohellohello , helloooo'
findtext = pattern.search(text)
print('Your text is: ', findtext.group())