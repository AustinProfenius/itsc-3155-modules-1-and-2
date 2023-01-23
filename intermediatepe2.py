def get_combined_dict(dict1,dict2):
  x = dict1.keys()
  y = dict2.keys()
  commonList = set(x).intersection(y)
  dict3 = dict()
  for z in commonList:
    temp1 = dict1.get(z)
    temp2 = dict2.get(z)
    temp3 = temp1 + temp2
    dict3[z]=temp3
  print(dict3)





my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)