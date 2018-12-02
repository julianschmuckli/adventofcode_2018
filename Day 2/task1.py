input = open("input.txt", "r").read()
boxes = input.split("\n")

two_occurrence = 0
three_occurrence = 0

for box in boxes:
    letters = list(box)
    if len(letters) != 0:
        letters.sort()

        previous_letter = ''
        current_occurrence = []

        two_count = False
        three_count = False

        for letter in letters:
            if previous_letter != letter:
                if len(current_occurrence) == 2 and two_count == False:
                    two_occurrence += 1
                    current_occurrence = []
                    two_count = True
                elif len(current_occurrence) == 3 and three_count == False:
                    three_occurrence += 1
                    current_occurrence = []
                    three_count = True
                else:
                    current_occurrence = []
            current_occurrence.append(letter)
            previous_letter = letter

        # Check for last letter
        if len(current_occurrence) == 2 and two_count == False:
            two_occurrence += 1
            current_occurrence = []
        elif len(current_occurrence) == 3 and three_count == False:
            three_occurrence += 1
            current_occurrence = []
print two_occurrence, " two occurrence(s), ", three_occurrence, " three occurrence(s)"
print "Checksum: ", two_occurrence * three_occurrence
