list1 = []
for x in range (0,5):
    while True:
        try:
            temp = int(input("Please enter int: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
        
            continue
        else:
        #age was successfully parsed!
        #we're ready to exit the loop.
            break
    list1.append(temp)
sum = 0
for x in list1:
    sum += x
print(sum)