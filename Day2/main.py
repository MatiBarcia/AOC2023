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
    

print(part1())