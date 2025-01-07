import re
# + has the same usage of * but it needs the pattern belongs to the text one time at least
pattern = re.compile(r'eu gosto de ((cagar)+)')
pattern1 = re.compile(r'eu gosto de (cagar)?')

#remove "cagarcagar" and your code will get an error bcz + needs at least one term of the pattern in the text
text = 'eu gosto de cagarcagar, eu gosto de amar, eu gosto de comer'

findtext = pattern.search(text)
findtext1 = pattern1.search(text)

print("Pattern with '+': ",findtext.group())
print("Pattern without '+' : ",findtext1.group())
