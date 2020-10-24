heavy = 0
light = 0
for i in range(1, 6):
    weight = float(input('{}# weight: '.format(i)))
    if weight > heavy:
        heavy = weight
        if light == 0:
            light = weight
    if weight < light:
        light = weight

print('Heaviest: ', heavy)
print('Lightest: ', light)
