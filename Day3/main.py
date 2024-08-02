import re

fileName = "input.txt"
symbols = ["*", "+", "%", "&", "$", "-", "=", "/", "#", "@"]
sum = 0

with open(fileName, "r") as f:
    previousLine = f.readline()  # primera linea nunca tiene simbolo
    currentLine = f.readline()
    followingLine = f.readline()

    while followingLine != "":
        for i, currentChar in enumerate(currentLine):
            if currentChar in symbols:
                if previousLine[i].isdigit():
                    before = False
                    after = False
                    if previousLine[i - 1].isdigit():
                        before = True
                    if previousLine[i + 1].isdigit():
                        after = True
                    if before and after:
                        numero = int(previousLine[i - 1 : i + 2])
                        print(numero)
                        sum += numero
                    elif before:
                        newLine = previousLine[: i + 1]
                        numero = int((re.search(r"\d+", newLine[::-1]).group())[::-1])
                        print(numero)
                        sum += numero
                    elif after:
                        newLine = previousLine[i:]
                        numero = int(re.search(r"\d+", newLine).group())
                        print(numero)
                        sum += numero
                    else:
                        sum += int(previousLine[i])

                elif previousLine[i - 1].isdigit():
                    newLine = previousLine[:i]
                    numero = int((re.search(r"\d+", newLine[::-1]).group())[::-1])
                    print(numero)
                    sum += numero

                if not previousLine[i].isdigit() and previousLine[i + 1].isdigit():
                    newLine = previousLine[i + 1 :]
                    numero = int(re.search(r"\d+", newLine).group())
                    print(numero)
                    sum += numero

                if currentLine[i - 1].isdigit():
                    newLine = currentLine[:i]
                    numero = int((re.search(r"\d+", newLine[::-1]).group())[::-1])
                    print(numero)
                    sum += numero
                if currentLine[i + 1].isdigit():
                    newLine = currentLine[i + 1 :]
                    numero = int(re.search(r"\d+", newLine).group())
                    print(numero)
                    sum += numero

                if followingLine[i].isdigit():
                    before = False
                    after = False
                    if followingLine[i - 1].isdigit():
                        before = True
                    if followingLine[i + 1].isdigit():
                        after = True
                    if before and after:
                        numero = int(followingLine[i - 1 : i + 2])
                        print(numero)
                        sum += numero
                    elif before:
                        newLine = followingLine[: i + 1]
                        numero = int((re.search(r"\d+", newLine[::-1]).group())[::-1])
                        print(numero)
                        sum += numero
                    elif after:
                        newLine = followingLine[i:]
                        numero = int(re.search(r"\d+", newLine).group())
                        print(numero)
                        sum += numero
                    else:
                        sum += int(followingLine[i])

                elif followingLine[i - 1].isdigit():
                    newLine = followingLine[:i]
                    numero = int((re.search(r"\d+", newLine[::-1]).group())[::-1])
                    print(numero)
                    sum += numero

                if not followingLine[i].isdigit() and followingLine[i + 1].isdigit():
                    newLine = followingLine[i + 1 :]
                    numero = int(re.search(r"\d+", newLine).group())
                    print(numero)
                    sum += numero

        previousLine = currentLine
        currentLine = followingLine
        followingLine = f.readline()

print(sum)
