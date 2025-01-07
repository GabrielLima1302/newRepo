import re
# | is used to say that others patterns can be found also
pattern = re.compile(r'(\(\d\d\))? (\d\d\d\d\d)(-)?(\d\d\d\d)|(\d\d\d\d)(-)?(\d\d\d\d)')
text = 'Today I sent a message to 995fg02-8874 but I could sent it to (21) 995022485'
phone = pattern.search(text)
print(phone.group())