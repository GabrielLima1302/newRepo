import re
# .search() method will return the match object of the first matched text in the searched string
# .findall() method will return a list of string of every match in the searched string
pattern = re.compile(r'\(\d\d\) \d\d\d\d\d-\d\d\d\d')
text = 'Phone numbers: (21) 99502-8874, (22) 98375-9999'
findtext = pattern.findall(text)
print('Phone numbers: ',' '.join(findtext))