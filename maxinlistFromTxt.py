numlist = []

fname = "maxlistinputs.txt"

def listinput(filename):
    filenew = open(filename, "r")
    filetext = filenew.read()
    filenew.close()

    outlist = []
    stopper = 0

    for x in range(len(filetext)):
        if filetext[x] == " ":
            outlist.append(int(filetext[stopper:x]))
            stopper = x+1
    
    return outlist

numlist = listinput(fname)



print(numlist)

def listmax(numbers=[]):
    
    return max(numbers)

print(listmax(numlist))
