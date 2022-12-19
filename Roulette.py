import random
listR = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
listB = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
print("Play options: odds, enen, 1to18, 19to36, 1st12, 2nd12, 3rd12, col1, col2, col3, red, black, digit(1-36)")
while True:
    found = False
    number = random.randint(1, 36)
    choice = input("Place your bet: ")
    choice = choice.replace(" ", "")
    choice = choice.lower()
    if(choice == "odds" or choice == "even"):
        check = number/2
        if(number == 0):
            print("You lose, the number was " + str(number))
            input()
        elif(choice == "odds"):
            if(check.is_integer() == False):
                print("You won, the number was " + str(number))
                input()
        elif(choice == "even"):
            if(check.is_integer()):
                print("You won, the number was " + str(number))
                input()
        else:
            print("You lose, the number was " + str(number))
            input()
    elif(choice == "1to18" or choice == "19to36"):
        if(number == 0):
            print("You lose, the number was " + str(number))
            input()
        elif(choice == "1to18"):
            if(number <= 18):
                print("You won, the number was " + str(number))
                input()
        elif(choice == "19to36"):
            if(number >= 19):
                print("You won, the number was " + str(number))
                input()
        else:
            print("You lose, the number was " + str(number))
            input()
    elif(choice == "1st12" or choice == "2nd12" or choice == "3rd12"):
        if(number == 0):
            print("You lose, the number was " + str(number))
            input()
        elif(choice == "1st12"):
            if(number <= 12):
                print("You won, the number was " + str(number))
                input()
        elif(choice == "2nd12"):
            if(number >= 13 and number <= 24):
                print("You won, the number was " + str(number))
                input()
        elif(choice == "3rd12"):
            if(number >= 25):
                print("You won, the number was " + str(number))
                input()
        else:
            print("You lose, the number was " + str(number))
            input()
    elif(choice == "col1" or choice == "col2" or choice == "col3"):
        if(number == 0):
            print("You lose, the number was " + str(number))
            input()
        elif(choice == "col1"):
            for i in range(12):
                if(number == 3*i+1):
                    print("You won, the number was " + str(number))
                    input()
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
                input()
        elif(choice == "col2"):
            for i in range(12):
                if(number == 3*i+2):
                    print("You won, the number was " + str(number))
                    input()
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
                input()
        elif(choice == "col3"):
            for i in range(12):
                if(number == 3*i+3):
                    print("You won, the number was " + str(number))
                    input()
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
                input()
    elif(choice == "red" or choice == "black"):
        if(number == 0):
            print("You lose, the number was " + str(number))
            input()
        if(choice == "red"):
            for item in listR:
                if(number == item):
                    print("You won, the number was " + str(number))
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
                input()
        elif(choice == "black"):
            for item in listB:
                if(number == item):
                    print("You won, the number was " + str(number))
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
                input()
    elif(choice.isdigit()):
        choice = int(choice)
        if(choice == number):
            print("You won, the number was " + str(number))
            input()
        else:
            print("You lose, the number was " + str(number))
            input()