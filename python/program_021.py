#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_21.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################

print("$ python primes_v1.0.py")
rangeStart = int(input("Enter first possible prime number to check. "))
rangeEnd = int(input("Enter las possible prime number to check. "))
primeNums = []
countPrimes = 0
for i in range(rangeStart, rangeEnd, +1):
    for j in range(2, i, +1):
        if (i % j == 0):
            break
    else:
        primeNums.append(i)
        countPrimes += 1
print("There are", countPrimes, "between", rangeStart, "and", rangeEnd, ".")
print("Prime numbers from", rangeStart, "to", rangeEnd,":", primeNums)

            
