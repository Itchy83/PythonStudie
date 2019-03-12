# Opgave 7 Sammenligning af for og while loops


# For loop til while loop
for x in range(0,11):
    print(x)

wx = 0

while wx < 10:
    wx += 1
    print(wx)



# While loop til for loop

print('----------------------------------------------------------')

tal = [20, 30, 40, 50, 60, 70]
index = 0
while tal[index] < 50:
    print(tal[index])
    index += 1

print('----------------------------------------------------------')

for fx in tal[0:3]:
    print(fx)

i = 0

for nr in tal:
    if nr < 50:
        print(nr)
    else:
        break

print('----------------------------------------------------------')


forloop = [1]
forloop2 = ('Undelig løkke')

for loop in forloop:
    print(loop)
    forloop.append(1)
    for loop2 in forloop2:
        forloop.remove(0)
        print(loop2)
        break

