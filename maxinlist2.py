numlist = []

def listinput():
    adder = 0
    listout = []

    while True:
        adder = int(input("What would you like to add to the list? "))

        listout.append(adder)

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
