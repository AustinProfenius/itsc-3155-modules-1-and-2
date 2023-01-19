list1 = []
word = ''
for x in range (0,5):
    temp = input('enter a word: ')
    list1.append(temp)

for x in list1:
    word+=x
    word+=' '

print(word)

