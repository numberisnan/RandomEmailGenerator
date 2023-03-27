import random

SAMPLESIZE = 70
TEXTFILENAME = "./text.txt"

with open(TEXTFILENAME, "r") as textFile:
    text = textFile.read()


newText = ";".join(random.sample(text.split(";"), SAMPLESIZE))

print(newText)

with open("./result.txt", "w") as outFile:
    outFile.write(newText)
