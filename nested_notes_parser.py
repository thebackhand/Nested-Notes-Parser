import sys
#User inputs the names of the notes files on the command line
notes = sys.argv[1]
output = sys.argv[2]


current_notefile = open(notes, "r")
outputfile = open(output, "w")
for line in current_notefile:
    print('lineis', line)
    #Count the number of leading tabs
    leading_tab_count = 0
    for character in line:
        if character=="\t":
            print('reached')
            leading_tab_count += 1
        else:
            print("character is", character)
            print(leading_tab_count, "leading_tab_count")
            break
    addendum = ""
    for value in range(leading_tab_count):
        addendum += "*"
    addendum += " "
    linestrip = line.strip()
    linestrip = addendum + linestrip + "\n"
    outputfile.write(linestrip)
current_notefile.close()
outputfile.close()
