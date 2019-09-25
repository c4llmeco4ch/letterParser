def parseText(filePath):
    charMap = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 
               'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 
               'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 
               'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 
               'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 
               'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 
               'y' : 0, 'z' : 0}
    with open(filePath) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                for char in word:
                    if not charMap.get(char[0], -1) == -1:
                        print("Found a {c}".format(c = char))
                        charMap[char] += 1
    return charMap

with open("./textList.txt") as texts:
    for line in texts.readlines():
        textMap = parseText(line)
        print("{title}\n{dashes}".format(title = line, dashes = "-" * len(line)))
        for pair in textMap.items():
            print("{key} | {val}".format(key = pair[0], val = pair[1]))