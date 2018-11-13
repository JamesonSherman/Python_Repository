#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_22.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
import math
print("$ pytthon primes_v2.0.py")
rangeEnd = int(input("Enter last possible prime number to check. " ))
countPrimes = 0;
primeNums = []
sieveOf_Eratosthenes = int(math.sqrt(rangeEnd) + 1)
                           
for i in range(2, (rangeEnd + 1), +1):
    for j in range(2, sieveOf_Eratosthenes, +1):
        if(i % j == 0 and i !=j):
            break
    else:
        primeNums.append(i)
        countPrimes += 1                   

print("Looking for prime numbers from 2 to", rangeEnd)
print("There are", countPrimes, "prime numbers between 2 and", rangeEnd)
print("Prime numbers from 2 to", rangeEnd, ":", primeNums)
