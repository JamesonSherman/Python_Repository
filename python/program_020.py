#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_20.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
list1 = [5, 38, 9, 45, 3, 38, 66, 83, 9, 5, 7, 98, 3]
uniqueList = []

for i in range(0,len(list1), +1):
    if (list1[i] not in uniqueList):
        uniqueList.append(list1[i])

print("$ python remove_dups_from_list_v0.py")
print("list =", list1)
print("unique_list =", uniqueList)
