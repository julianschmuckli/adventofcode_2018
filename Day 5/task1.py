input = open("input.txt", "r").read()
input = list(input)

if input[len(input)-1] == "\n":
    del input[-1];

while True:
    changed_round = False
    for i in range(0, len(input)-1):
        current = input[i]
        next = input[i+1]

        if current != None and next != None and current != next and current.upper() == next.upper():
            input[i] = None
            input[i+1] = None
            changed_round = True

    input = filter(None, input)

    if changed_round == False:
        break;

print "Total left units: ", len(input)
