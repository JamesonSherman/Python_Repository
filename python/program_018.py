#####################################################
###  Name:          James Sherman
###  Student ID:    900114
###  Assignment:    Problem Set 2
###  Program Name:  program_018.py
###  Due Date:      October 11, 2018 1:15pm
#####################################################
print("$ python odd.or.even.py")
def test_Odd_Even():
    testNum = int(input("Enter integer to test if odd or even?" ))
    if (testNum % 2 == 0):
        print(testNum, "is an even number.")
    else:
        print(testNum, "is not an even number.")
    runagain = input("Would you like to test another number?" )
    if ((runagain == "YES" or runagain == "yes") or (runagain == "Yes")):
        test_Odd_Even()
    elif(runagain == "Y" or runagain == "y"):
        test_Odd_Even()

test_Odd_Even()
