input = open("input.txt", "r").read()
frequencies = input.split("\n")

value = 0

for frequency in frequencies:
    sign = frequency[:1]
    if frequency != '':
        number = int(frequency.replace("+","").replace("-",""))
        if sign == '+':
            value += number
        elif sign == '-':
            value -= number

print value
