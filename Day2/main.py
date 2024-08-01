# ACORDATE DEL NUMERO DE GAME

with open("Day2/input.txt", "r") as f:
    line = f.readline()
    line.find(":")
    lineSplit = line[line.find(":")+1:]
    lineSplit = lineSplit.split(";") # usa mas variables paja

    for line in lineSplit:
        print(line)