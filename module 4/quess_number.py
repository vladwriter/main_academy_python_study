import random


START_PLACEHOLDER = "Try to quess the number from 0 to 100:"
TO_MUCH_RESULT = "To much"
TO_LESS_RESULT = "To less"


counter = 1
ansver = False
random_num = random.randint(1, 100)


while ansver != random_num:
    TRY = "Try #{0}: {1}".format(counter, ansver)
    ansver = int(input(START_PLACEHOLDER))
    if ansver > random_num:
        print(TRY)
        print(TO_MUCH_RESULT)
        counter += 1
    elif ansver < random_num:
        print(TRY)
        print(TO_LESS_RESULT)
        counter += 1
    else:
        print("You have guessed from {} try".format(counter))
        print("{} is true".format(random_num))
