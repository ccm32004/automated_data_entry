import pyperclip

def reverse(string):
    string = string.replace('-', ' ')
    return string

here = input("enter string pls ")

pyperclip.copy(str(reverse(here)))
test = pyperclip.paste()
print(test)