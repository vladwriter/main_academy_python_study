import random

random_num = random.randint(1, 100)
counter = 1
ansver = False
while ansver != random_num:
    ansver = int(input('Try to quess the number from 0 to 100:'))
    if ansver > random_num:
        print("Try #%s: %s" % (counter, ansver))
        print("To much")
        counter += 1
    elif ansver < random_num:
        print("Try #%s: %s" % (counter, ansver))
        print("To less")
        counter += 1
    else:
        print("You have guessed from %s try" % counter)
        print("%s is true" % random_num)
