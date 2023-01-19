mainList = []
smallList = []

temp = input('enter a string: ')

for x in range (0,len(temp)):
    smallList.append(temp[x])
    if len(smallList) == 3 or x == len(temp)-1:
        mainList.append(smallList)
        smallList = []
print(mainList)