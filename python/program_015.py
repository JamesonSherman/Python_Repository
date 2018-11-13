#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_015.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
print("$ python.count.even.py", "Please enter 6 numbers to be tested odd/even", sep ="\n")

testList =[]
for i in range(0,6,+1):
    elem = int(input("Enter integer to test if od or even? "))
    testList.append(elem)

evenCount = 0
oddCount = 0;
for elem in testList:
    if (elem % 2 == 0):
        evenCount += 1
    elif (elem % 2 != 0):
        oddCount += 1

print("You entered", oddCount, "odd numbers")
print("You entered", evenCount, "even numbers")
