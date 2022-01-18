import random

def yourNumber():
    randNum = random.randint(1, 10000)
    print(randNum)
    if randNum > 7500:
        print("You got a high number!")
    elif randNum > 2500 and randNum <= 7500:
        print("Pretty average number.")
    else:
        print("You a low baller..")
yourNumber()
