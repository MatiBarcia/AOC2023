import sys

def part1(file):
    f = open(file, "r")
    sum = 0

    for line in f:
        maxIndex = -sys.maxsize-1
        minIndex = sys.maxsize  
        for i in range(1, 10):
            index = line.find(str(i))
            if index >= 0:
                if index < minIndex:
                    minIndex = index
                    min = i
        
            index = line.rfind(str(i))
            if index >= 0:
                if index > maxIndex:
                    maxIndex = index
                    max = i
        
        sum += int(str(min) + str(max))

    f.close()
    return sum

def part2(file):
    f = open(file, "r")
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0

    for line in f:
        maxIndex = -sys.maxsize-1
        minIndex = sys.maxsize  
        for i in range(1, 10):
            index = line.find(numbers[i])
            if index >= 0:
                if index < minIndex:
                    minIndex = index
                    min = i

            index = line.find(str(i))
            if index >= 0:
                if index < minIndex:
                    minIndex = index
                    min = i
            
            index = line.rfind(numbers[i])
            if index >= 0:
                if index > maxIndex:
                    maxIndex = index
                    max = i

            index = line.rfind(str(i))
            if index >= 0:
                if index > maxIndex:
                    maxIndex = index
                    max = i
        
        sum += int(str(min) + str(max))
        
    f.close()
    return sum

print(part1("Day1/input.txt"))
print(part2("Day1/input.txt"))