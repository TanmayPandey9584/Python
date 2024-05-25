import copy
li1 = [1, 2, [3, 5], 4]
li2 = copy.copy(li1)
li3 = copy.deepcopy(li1)
li1[2][0]=4
print("li2 ID: ", id(li2),'\n',"Value: ", li2)
print("li3 ID: ", id(li3),'\n',"Value: ", li3)