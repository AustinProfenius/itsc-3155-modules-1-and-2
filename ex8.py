ogList = []
appearOnce = []
for x in range (0,10):
    temp = input('please enter an int:')
    ogList.append(temp)
for x in range(0,10):
    if ogList.count(ogList[int(x)]) == 1:
        appearOnce.append(ogList[int(x)])
print(ogList)
print(appearOnce)