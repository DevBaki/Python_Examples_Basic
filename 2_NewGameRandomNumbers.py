import random




def new_game():
    global num
    print('New game starts!!!')


def range_of_100():
    global num
    num = random.randrange(0, 100)
    print('your range is 0-100')


def range_of_1000():
    global num
    num = random.randrange(0, 1000)
    print("Your range is 0-1000")


def guess_number():
    your_number = input()
    if num > int(your_number):
        print('you guess more than random number')

    elif num < int(your_number):
        print('you guess less than random number')

    elif num == int(your_number):
        print('Great , you won')


range_of_100()
guess_number()
