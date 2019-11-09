TAKENFILENAME = "./taken.txt"
RESULTFILENAME = "./result.txt"

with open(RESULTFILENAME, "r") as rFile:
    recipients = rFile.read()

with open(TAKENFILENAME, "r") as tFile:
    takenList = list(map(lambda s:s.replace("\n",""), tFile.readlines()))

newRecipients = []

for r in recipients.split(";"):
    tInR = False
    for t in takenList:
        if (t in r):
            print(t + " has already taken!")
            tInR = True
            break
    not tInR and newRecipients.append(r)

with open("./newRecipients.txt", "w") as rFile:
    rFile.write(";".join(newRecipients))