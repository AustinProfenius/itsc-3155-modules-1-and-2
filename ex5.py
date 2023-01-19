from pickle import FALSE


list1=[]
list2=[]
commonList=[]

for x in range(0,5):
    temp = input('enter number for first list:')
    list1.append(temp)

for x in range(0,5):
    temp = input('enter number for second list:')
    list2.append(temp)

print('First list:',list1)
print('Second list:',list2)

commonList = set(list1).intersection(list2)
print('Common list:',commonList)
