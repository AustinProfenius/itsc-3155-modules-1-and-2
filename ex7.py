temp = ""
list1 = []
even = []
while temp != "QUIT":
    temp = input('Enter a number or QUIT to quit: ')
    if temp != "QUIT":
        list1.append(temp)
for x in range(0,len(list1)):
    y = list1[int(x)]
    y = int(y)
    if y%2 == 0:
        z = list1[x]
        even.append(z)
print(list1)
print(even)