li = [1, 4, 2, 1, 6, 2, 8, 3, 5]
ln = [100, 99, 100, 88, 100, 99, 100, 88, 100, 99, 100, 88, 100, 99, 100, 88]
array = [2, 1, 2, 4, 43, 65, 34, 11, 4, 21, 1, 61, 21, 8, 30, 5, 4]
ls = [2, 1, 2, 4, 43, 65, 34, 11, 4, 21, 1, 61, 21,
         8, 30, 5, 4, 21, 8, 30, 5, 4, 32, 12, 14, 15, 23]

# var = a, b, x, y, z
# Moving var = x, y, z

b = len(array) - 1
a = len(array) - 2
x = 0
y = 2
z = (x + y) // 2

# Reads the first two nunbers [0,1] in arrayst array

maximumf = max(array[0], array[1])
if maximumf == array[0]:
    print('\n\tpeak = {}'.format(array[0]))


# Starts reading in the second number [1] till the end
# but don't the last two var([a,b])

while y <= len(array) - 1:
    z = (x + y) // 2
    maximum = max(array[x], array[z], array[y])
    if maximum == array[z]:
        print('\n\tpeak = {}'.format(array[z]))
    x += 1
    y += 1

# reads the last two numbers var([a,b])

maximumf = max(array[a], array[b])
if maximumf == array[b]:
    print('\n\tpeak = {}'.format(array[b]))

print('\n\tfinished!')
