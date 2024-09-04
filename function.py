import calendar

def automate(string):
    string = string.replace(',', '-')
    string = string.replace(' ', '-')
    string = string.replace('’', '')
    string = string.replace('–', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
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

    string += ".pdf"
    return string

def removeSpace(str):
    str = str.replace('  ', ' ')
    return str

def getDate(label):
    fixed = label.replace('(', '')
    fixed = fixed.replace(')', '')
    fixed = fixed.replace(',', '')

    array = fixed.split(' ') 
    
    for i in range (0,len(array)):
        if array[i] == "January" or array[i] == "janvier":
            array[i] = "01"
        elif array[i] == "February" or array[i] == "fevrier" or array[i] == "fevrier":
            array[i] = "02"
        elif array[i] == "March" or array[i] == "mars":
            array[i] = "03"
        elif array[i] == "April" or array[i] == "avril":
            array[i] = "04"
        elif array[i] == "May" or array[i] == "mai":
            array[i] = "05"
        elif array[i] == "June" or array[i] == "juin":
            array[i] = "06"
        elif array[i] == "July" or array[i] == "juillet":
            array[i] = "07"
        elif array[i] == "August" or array[i] == "août":
            array[i] = "08"
        elif array[i] == "September" or array[i] == "septembre":
            array[i] = "09"
        elif array[i] == "October" or array[i] == "octobre":
            array[i] = "10"
        elif array[i] == "November" or array[i] == "novembre":
            array[i] = "11"
        elif array[i] == "December" or array[i] == "decembre":
            array[i] = "12"
    
    date_array = []
    for item in array:
       if item.isnumeric():
           date_array.append(item)
     
    dateIndex = 1

    for i in range (0,len(date_array)):
        if len(date_array[i]) < 2:
            if(i == 0):
                dateindex = 0

    
    if dateIndex == 0:
        date_array[1] = calendar.month_name[int(date_array[1])]
    else:
        date_array[0] = calendar.month_name[int(date_array[0])]

    date_array[1] += ","
    myString = ' '.join(date_array)
    

   
    return myString
        
