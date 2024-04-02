# from GCD import GCD
import math
import random

def MLT(n,k=-1):
    if (k == -1):
        k = int(math.log(n))
    if (n <= 2):
        print(f"{n} is a prime number")
        return True
    if (n % 2 == 0):
        print(f"{n} is a composite number")
        return False
    s = 1
    d = (n - 1) / 2
    while (d % 2 == 0):
        d /= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = exponentiation(int(a), int(d), int(n))
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = exponentiation(int(x), int(2), int(n))
            if x == n - 1:
                break
        else:
            print(f"{n} is a composite number")
            return False
    print(f"{n} is PROBABLY a prime number")
    return True
def exponentiation(number, power, mod):
    if (power == 0):
        return 1;
    if (power == 1):
        return number % mod

    t = exponentiation(number, int(power / 2),mod)
    t = (t * t) % mod

    # if exponent is
    # even value
    if (power % 2 == 0):
        return t

    # if exponent is
    # odd value
    else:
        return ((number % mod) * t) % mod

def KeyboardInput():
    print("Please input the number and an amount of rounds (1 by default)")
    userInput = input()
    return (ParseStringIntoFloat(userInput))
def FileInput():
    print("Please input the name of the .txt file with values:")
    userInput = input()
    floatListList=[]
    fileStrings=[]
    try:
        with open(f"{userInput}.txt") as file:
            fileStrings=file.readlines()
        for i in fileStrings:
            floatListList.append(ParseStringIntoFloat(i))
        return floatListList
    except FileNotFoundError:
        print("Please input the name of an existing file\n")
        Run()

def ParseStringIntoFloat(string):
    inputList = string.split(" ")
    floatInputList = []
    for i in inputList:
        try:
            floatInputList.append(float(i))
        except ValueError:
            print("Please input only 2 numbers\n")
            Run()
    if (len(floatInputList)>2 or len(floatInputList)<1):
        print("Please input only 1 or 2 numbers per line\n")
        Run()
    return floatInputList


def Run():
    print("Main menu: \n1.Keyboard Input\n2.File Input\n\nInput: ")
    menuSelection=int(input())
    userInput=""
    if menuSelection==1:
        userInput= KeyboardInput()
        if(len(userInput)==1):
            MLT(userInput[0])
        elif(len(userInput)==2):
            MLT(userInput[0],int(userInput[1]))
    elif menuSelection==2:
        userInput = FileInput()
        for i in userInput:
            if (len(i) == 1):
                MLT(i[0])
            elif (len(i) == 2):
                MLT(i[0], int(i[1]))
    Run()
Run()

