import random

numlist = []

def listinput():
    adder = 0
    listout = []

    while True:
        adder = random.randint(1, 500)

        listout.append(adder)

        print(adder)

        print("Would you like to add another number? (y/n)")
        ans = input()

        if ans == "y":
            pass
        elif ans == "n":
            break
        else: 
            print("Could not understand answer. Closing...")
            break
    return listout


numlist = listinput()

print(numlist)

def listmax(numbers=[]):
    
    return max(numbers)

print(listmax(numlist))
