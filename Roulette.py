import random, json, os
connector = open("./data.json")
imported = json.load(connector)
connector.close()
listR = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
listB = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
while True:
    os.system("cls")
    print("Play options: odds, enen, 1to18, 19to36, 1st12, 2nd12, 3rd12, col1, col2, col3, red, black, digit(1-36)")
    print("Your saldo is " + str(imported["money"]))
    found = False
    won = False
    multiplier = 1
    number = random.randint(1, 36)
    modeChoice = input("Choose game mode: ")
    betChoice = input("Place your bet: ")
    try:
        betChoice = int(betChoice)
    except ValueError:
        continue
    if int(betChoice) > imported["money"]:
        continue
    modeChoice = modeChoice.replace(" ", "")
    modeChoice = modeChoice.lower()
    if(modeChoice == "odds" or modeChoice == "even"):
        check = number/2
        if(number == 0):
            print("You lose, the number was " + str(number))
        elif(modeChoice == "odds"):
            if(check.is_integer() == False):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 2
        elif(modeChoice == "even"):
            if(check.is_integer()):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 2
        else:
            print("You lose, the number was " + str(number))
    elif(modeChoice == "1to18" or modeChoice == "19to36"):
        if(number == 0):
            print("You lose, the number was " + str(number))
        elif(modeChoice == "1to18"):
            if(number <= 18):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 2
        elif(modeChoice == "19to36"):
            if(number >= 19):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 2
        else:
            print("You lose, the number was " + str(number))
    elif(modeChoice == "1st12" or modeChoice == "2nd12" or modeChoice == "3rd12"):
        if(number == 0):
            print("You lose, the number was " + str(number))
        elif(modeChoice == "1st12"):
            if(number <= 12):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 3
        elif(modeChoice == "2nd12"):
            if(number >= 13 and number <= 24):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 3
        elif(modeChoice == "3rd12"):
            if(number >= 25):
                print("You won, the number was " + str(number))
                won = True
                multiplier = 3
        else:
            print("You lose, the number was " + str(number))
    elif(modeChoice == "col1" or modeChoice == "col2" or modeChoice == "col3"):
        if(number == 0):
            print("You lose, the number was " + str(number))
        elif(modeChoice == "col1"):
            for i in range(12):
                if(number == 3*i+1):
                    print("You won, the number was " + str(number))
                    won = True
                    multiplier = 3
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
        elif(modeChoice == "col2"):
            for i in range(12):
                if(number == 3*i+2):
                    print("You won, the number was " + str(number))
                    won = True
                    multiplier = 3
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
        elif(modeChoice == "col3"):
            for i in range(12):
                if(number == 3*i+3):
                    print("You won, the number was " + str(number))
                    won = True
                    multiplier = 3
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
    elif(modeChoice == "red" or modeChoice == "black"):
        if(number == 0):
            print("You lose, the number was " + str(number))
        if(modeChoice == "red"):
            for item in listR:
                if(number == item):
                    print("You won, the number was " + str(number))
                    won = True
                    multiplier = 2
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
        elif(modeChoice == "black"):
            for item in listB:
                if(number == item):
                    print("You won, the number was " + str(number))
                    won = True
                    multiplier = 2
                    found = True
            if(found == False):
                found = False
                print("You lose, the number was " + str(number))
    elif(modeChoice.isdigit()):
        modeChoice = int(modeChoice)
        if(modeChoice == number):
            print("You won, the number was " + str(number))
            won = True
            multiplier = 36
        else:
            print("You lose, the number was " + str(number))
    if won:
        imported["money"] = (betChoice * multiplier) + (imported["money"] - betChoice)
    else:
        imported["money"] = imported["money"] - betChoice
    print("Your saldo is " + str(imported["money"]))
    input()
    if(imported["money"] < 1):
        imported["money"] = 1
    connector = open("C:/python_workspace/Roulette/data.json", "w", encoding="utf-8")
    json.dump(imported, connector)
    connector.close()
