temp = input("enter a string: ")

listA = []
listB = []
listC = []

for x in temp:
    if x.isupper():
        listA.append(x)
    if x.islower():
        listB.append(x)

for x in listA:
    print(x,end='')
for x in listB:
    print(x,end='')
