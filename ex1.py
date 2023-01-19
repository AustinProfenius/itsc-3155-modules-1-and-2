x = input("Enter a number between 0-100: ")
y = int(x) 
if y<60:
    print('Your grade is F')
elif y<69:
    print('Your grade is D')
elif y<79:
    print('Your grade is C')
elif y<89:
    print('Your grade is B')
else:
    print('Your grade is A')