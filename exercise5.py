#List
myMixedTypeList=[45, 290578, 1.02, True, "My dog is on the bed.", "45"]

print(myMixedTypeList)

#for loop statement to traverse the list and print the data type for each item in the list
for item in myMixedTypeList:print("{} is of the data type {}".format(item,type(item)))
