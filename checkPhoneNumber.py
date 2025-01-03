#import string
def isPhoneNumber(text):
    #clean_text = text.translate(str.maketrans(' ',' ', string.punctuation + " ")) #.translation remove punctuation and spaces // str.maketrans() maps each punctuation and space to None // string.punctuation contains all common punctuation character
    #print(clean_text)

    if len(text)!=10:
        return False

    for i in range (0, 5):
        if not text[i].isdecimal():
            return False

    if text[5] != "-":
        return False

    for i in range (6, 10):
        if not text[i].isdecimal():
            return False

    return True
t = input("Type: ")
for i in range (len(t)):
    c = t[i:i+10] #c receives a string that starts at i and goes till i+10 of the "t" text
    if isPhoneNumber(c): #check if "c" is a phone number
        print(c+" is a phone number")
"""print('99502-8874 is a phone number:')
print(isPhoneNumber('99502-8874'))
print('AAA is a phone number')
print(isPhoneNumber('AAA'))"""