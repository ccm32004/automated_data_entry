import pyperclip

def automate(string):
    string = string.replace(',', '-')
    string = string.replace(' ', '-')
    string = string.replace('’', '')
    string = string.replace('–', '')
    string = string.replace(')', '')
    string = string.replace('(', '')
    x = 0
    while (x < len(string)-2):
        if (string[x] == string[x+1]) and (string[x] == '-'):
            original = x
            y = x + 2
            
            while(string[x] == string[y]):
                y += 1
            
            difference = y - x
            string = string[0:x+1] + string[x + difference: len(string)]

        x += 1

    #string += ".pdf"
    return string

pog = input("string pls: ") 
pyperclip.copy(str(automate(pog)))
test = pyperclip.paste()
print(test)

