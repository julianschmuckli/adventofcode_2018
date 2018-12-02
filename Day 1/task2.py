input = open("input.txt", "r").read()
frequencies = input.split("\n")

value = 0
value_found = False
history = []

# This script takes some minutes to execute

def calcDouble(value):
    global value_found
    for frequency in frequencies:
        sign = frequency[:1]
        if frequency != '':
            number = int(frequency.replace("+","").replace("-",""))
            if sign == '+':
                value += number
            elif sign == '-':
                value -= number
            if value in history:
                value_found = True
                break;
            else:
                history.append(value)
    print value
    if value_found == False:
        calcDouble(value)
    return value

value = calcDouble(value)
print "The last value above is your result"
