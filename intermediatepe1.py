
list1 = []
list2 = []
x = ''
## while x != 'q':
 #   x=input('please enter an int or press q: ')
 #   if x != 'q':
 #       list1.append(x)
def get_unique_list(list1):
    list2 = []
    for x in list1:
        if list2.count(x)<1:
            list2.append(x)  
    return list2


my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)