def check(first,second):
    fin = []
    for i in range(len(second)):
        for j in range(len(second[i])):
            fin.append(second[i][j])        # Gathering all the elements of the sub sequence.
    
    for i in first:
        if i not in fin:                    # If any of the element is not present.
            return False 
    return True                             # If all are present.

first = [123,34,45,13,6]
second = [[123,34],[45,13],[6]]

print(check(first,second))