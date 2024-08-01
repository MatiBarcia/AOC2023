import re

fileName = 'input.txt'
numGames = sum(1 for _ in open(fileName))

def part1():
    with open(fileName, "r") as f:
        sum = 0
        for id in range(1, numGames+1):
            line = f.readline()
            # print("Game ", end=str(id)+"\n")

            gameSplit = line[line.find(":")+1:]
            setSplit = gameSplit.split(";")
            valid = True

            for set in setSplit:
                colorSplit = set.split(",")
                for color in colorSplit:
                    if((color.find("red") != -1) & valid):
                        amountRed = re.search(r'\d+', color).group()
                        if(int(amountRed) > 12):
                            valid = False
                            break

                    if((color.find("green") != -1) & valid):
                        amountGreen = re.search(r'\d+', color).group()
                        if(int(amountGreen) > 13):
                            valid = False
                            break
                    
                    if((color.find("blue") != -1) & valid):
                        amountBlue = re.search(r'\d+', color).group()
                        if(int(amountBlue) > 14):
                            valid = False
                            break
            
            if(valid):
                sum += id
                # print("Se suma ", end=str(id)+"\n")
        
        return sum
    
def part2():
    with open(fileName, "r") as f:
        sum = 0
        for id in range(1, numGames+1):
            line = f.readline()
            # print("Game ", end=str(id)+"\n")

            gameSplit = line[line.find(":")+1:]
            setSplit = gameSplit.split(";")

            minRed = 1
            minGreen = 1
            minBlue = 1

            for set in setSplit:
                colorSplit = set.split(",")
                for color in colorSplit:
                    if((color.find("red") != -1)):
                        amountRed = int(re.search(r'\d+', color).group())
                        if(amountRed > minRed):
                            minRed = amountRed

                    if((color.find("green") != -1)):
                        amountGreen = int(re.search(r'\d+', color).group())
                        if(amountGreen > minGreen):
                            minGreen = amountGreen
                    
                    if((color.find("blue") != -1)):
                        amountBlue = int(re.search(r'\d+', color).group())
                        if(amountBlue > minBlue):
                            minBlue = amountBlue
            
            # print("GAME ", end=str(id)+"\n")
            # print("Red ", end=str(minRed)+"\n")
            # print("Green ", end=str(minGreen)+"\n")
            # print("Blue ", end=str(minBlue)+"\n\n")
            sum += minRed * minGreen * minBlue
        
        return sum

print("Parte 1: ", end=str(part1())+"\n")
print("Parte 2: ", end=str(part2())+"\n\n")