temp = input("enter a string")
list1 = []
for x in range (len(temp)-1,-1,-1):
    list1.append(temp[x])
for x in list1:
    print(x,end="")

