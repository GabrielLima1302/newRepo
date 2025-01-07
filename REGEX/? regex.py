import re
# ? is used after a pattern that can be found optionally, the pattern that proceeds the ? is the main choice
pattern = re.compile(r"(\(\d\d\)) (\d\d\d\d\d-\d\d\d\d)?(\d\d\d\d-\d\d\d\d)")
text = 'Today I sent the message to (21) 99502-8874 but I could send it to (22) 9502-9984'
phone = pattern.search(text)
print(phone.group())