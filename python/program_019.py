#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_019.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
list1 = [21, 55, 34, 5, 92, 2, 8, 13, 55, 1, 89]
list2 = [55, 3, 1, 83, 92, 1, 63, 44, 1, 19]
intersectingList = []

for i in range(0, len(list1), +1):
    for j in range(0,len(list2), +1):
        count = 0
        if(list1[i] == list2[j] and list1[i] not in intersectingList):
            intersectingList.append(list1[i])
                
print("$ python list_intersections.py")
print("list1 =", list1)
print("list2 =", list2)
print("intersecting list without duplications = ", intersectingList)
