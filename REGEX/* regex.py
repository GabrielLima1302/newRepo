import re
# * is used to create a pattern that can be repeated over and over along the sequence, but the pattern may not belong to the text
pattern = re.compile(r'eu gosto de (cagar)*,')
pattern1 = re.compile(r'eu gosto de (cagar)')

text = 'eu gosto de cagarcagarcagar, eu gosto de amar, eu gosto de comer'

findtext = pattern.search(text)
findtext1 = pattern1.search(text)

print("Pattern with '*': ",findtext.group())
print("Pattern without '*' : ",findtext1.group())