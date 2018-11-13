#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_016.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
print("$ python divors.py")
testelem = 2
divisors = []
for i in range (2, 31, +1):
    for j in range(1, 31, +1):
        if (i % j == 0):
            divisors.append(j)
    print("The divisors of", i, "are", divisors)
    divisors.clear()
