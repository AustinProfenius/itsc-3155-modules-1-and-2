from telnetlib import PRAGMA_HEARTBEAT


x = input('Please enter a String:')
y = input('Please enter another Sting:')
if x.find(y)>0:
    print('True')
elif y.find(x)>0:
    print('True')
else:
    print('False')
