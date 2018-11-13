#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_23.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
originalList = [5, 38, 9, 45, 3, 38, 66, 83, 9, 5, 7, 98, 3]
newList = []

print("$ python remove_dups_from_list_v1.py")
print("original list:", originalList)

for i in range(len(originalList)):
    for j in range(0, (len(originalList) - i - 1)):
        if originalList[j] > originalList[j +1]:
            originalList[j], originalList[j + 1] = originalList[j + 1], originalList[j]
 
print("sorted list:", originalList)

for i in range(len(originalList)):
    if originalList[i] not in newList:
        newList.append(originalList[i])

print("list without duplicates", newList)
