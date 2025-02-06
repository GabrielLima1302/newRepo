import re

# you can create you own character classes using square brackets "[]", example: [aeiouAEIOU]
# you can also include ranges of letters or numbers by using a hyphen, example: [a-zA-Z0-9] or [0-5.]
# using a ^ after the first bracket you can match all the characters that are not in the character class
pattern = re.compile(r'[aeiouAEIOU]')
pattern1 = re.compile(r'[^aeiouAEIOU]')
pattern2 = re.compile(r'[0-5]')

text = 'how are you going today? 21995028874.'

findtext = pattern.findall(text)
findtext1 = pattern1.findall(text)
findtext2 = pattern2.findall(text)


print(*findtext)
print(*findtext1)
print(*findtext2)

