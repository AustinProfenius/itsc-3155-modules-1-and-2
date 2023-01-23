
def keepTrackOfLetters (input):
    dict1 = dict()
    for x in input:
        if x != ' ':
            dict1[x] = input.count(x)
    print(dict1)

temp = input('enter a String; ')
print(keepTrackOfLetters(temp))