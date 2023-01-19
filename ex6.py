x=input('enter a row num from 1 to 5:')
y=input('enter a col num from 1 to 5:')
x = int(x)
y = int(y)

for a in range (1,6):
    print("")
    for b in range(1,6):
        if x == a and b == y:
            print('1', end=" ")
        else:
            print('0', end=" ")
          