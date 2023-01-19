x = input('enter an integer:')
y = int(x)
a = []
z = 1
temp = 0
while z<=y:
    print('enter number', z,':')
    temp = input()
    a.append(temp)
    z = z+1
print(a)
total = 0
for x in range(0,y):
    total = total + int(a[x])
print('average:', total/y)
