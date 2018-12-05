input = open("input.txt", "r").read()
tasks = input.split("\n")

# Creates a list containing 100000 lists, each of 100000 items, all set to 0
print "Generating map..."
w, h = 1000, 1000;
matrix = [[0 for x in range(w)] for y in range(h)]

count_inches = 0

for task in tasks:
    if task != "":
        parts = task.split(" ")
        number = parts[0].replace("#","")
        coordinates = parts[2].replace(":","").split(",");
        size = parts[3].split("x");

        for x in range(int(coordinates[0]), int(coordinates[0]) + int(size[0])):
            for y in range(int(coordinates[1]), int(coordinates[1]) + int(size[1])):
                print "Placing: ", x, "," , y
                if matrix[x][y] == 0:
                    matrix[x][y] = number
                else:
                    if matrix[x][y] != "X":
                        matrix[x][y] = "X"
                        count_inches += 1
                        print "Found double inch: ", x, ",", y
                    else:
                        print "Duplicate inch: ", x, ",", y

print "Total duplicate inches: ", count_inches
