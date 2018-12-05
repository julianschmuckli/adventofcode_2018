input = open("input.txt", "r").read()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result_alphabet = []

for i in range(0, len(alphabet)):
    print "Processing ", alphabet[i]
    temp_input = input.replace(alphabet[i].upper(),'')
    temp_input = temp_input.replace(alphabet[i].lower(),'')
    temp_input = list(temp_input)

    if temp_input[len(temp_input)-1] == "\n":
        del temp_input[-1];

    while True:
        changed_round = False
        for i in range(0, len(temp_input)-1):
            current = temp_input[i]
            next = temp_input[i+1]

            if current != None and next != None and current != next and current.upper() == next.upper():
                temp_input[i] = None
                temp_input[i+1] = None
                changed_round = True

        temp_input = filter(None, temp_input)

        if changed_round == False:
            break;

    result_alphabet.append(len(temp_input))

shortest = 50000
for current in result_alphabet:
    if(current < shortest):
        shortest = current

print result_alphabet
print "Shortest unit length: ", shortest
