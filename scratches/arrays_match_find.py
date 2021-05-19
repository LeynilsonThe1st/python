array = [6, 6, 4, 4, 5, 6, 7, 8, 8, 9, 2, 2]
newArray = []
a = 0
b = 1
for x in array:
    if b == len(array):
        break
    elif array[a] == array[b]:
        print(array[a], array[b])
        newArray.append(array[a])
    a += 1
    b += 1


print(newArray)