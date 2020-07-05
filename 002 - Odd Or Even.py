import random
import sys


def rerun():
    """Asking if user wants to run again"""
    choice = input('Do you wanna rerun again?: <Y> Yes | <Any Key> Exit\n')
    choice = choice.upper()
    if choice == 'Y':
        game()
    else:
        sys.exit(0)


def game():
    print('\n//////////////////////////')
    """Automate that shit"""
    num2 = random.randint(1, 100)
    num4 = random.randint(1, 100)
    print(f'First random number is between 1 - 100\n1st number is: {num2}')
    print(f'Second random number is between 1 - 100\n2nd number is: {num4}')
    print('//////////////////////////')
    calc(num2, num4)


def calc(num2, num4):
    oddOrEvenNum2 = num2 % 2
    oddOrEvenNum4 = num4 % 2
    multipleOf4Num2 = num2 % 4
    multipleOf4Num4 = num4 % 4
    checkDiv = num2 % num4
    prints(oddOrEvenNum2, oddOrEvenNum4, multipleOf4Num2, multipleOf4Num4, checkDiv, num2, num4)


def prints(oddOrEvenNum2, oddOrEvenNum4, multipleOf4Num2, multipleOf4Num4, checkDiv, num2, num4):
    """Prints"""
    if oddOrEvenNum2 == 0 and oddOrEvenNum4 == 0:
        if multipleOf4Num2 == 0 and multipleOf4Num4 == 0:
            print('Num1: {} is even and divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 != 0:
            print('Num1: {} is even but not divisible by 4.'.format(num2)
                  + '\nNum2: {} is even but not divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 == 0:
            print('Num1: {} is even but not divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and divisible by 4.'.format(num4))
        else:
            print('Num1: {} is even and divisible by 4.'.format(num2)
                  + '\nNum2: {} is even but not divisible by 4.'.format(num4))

    elif oddOrEvenNum2 != 0 and oddOrEvenNum4 != 0:
        if multipleOf4Num2 == 0 and multipleOf4Num4 == 0:
            print('Num1: {} is not even but divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd but divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 != 0:
            print('Num1: {} is odd and not divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd and not divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 == 0:
            print('Num1: {} is odd and not divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd but divisible by 4.'.format(num4))
        else:
            print('Num1: {} is odd but divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd and not divisible by 4.'.format(num4))

    elif oddOrEvenNum2 != 0 and oddOrEvenNum4 == 0:
        if multipleOf4Num2 == 0 and multipleOf4Num4 == 0:
            print('Num1: {} is odd but divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 != 0:
            print('Num1: {} is odd and not divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and not divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 == 0:
            print('Num1: {} is odd and not divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and divisible by 4.'.format(num4))
        else:
            print('Num1: {} is odd but divisible by 4.'.format(num2)
                  + '\nNum2: {} is even and not divisible by 4.'.format(num4))

    elif oddOrEvenNum2 == 0 and oddOrEvenNum4 != 0:
        if multipleOf4Num2 == 0 and multipleOf4Num4 == 0:
            print('Num1: {} is even and divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd but divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 != 0:
            print('Num1: {} is even but not divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd and not divisible by 4.'.format(num4))
        elif multipleOf4Num2 != 0 and multipleOf4Num4 == 0:
            print('Num1: {} is even but not divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd but divisible by 4.'.format(num4))
        else:
            print('Num1: {} is even and divisible by 4.'.format(num2)
                  + '\nNum2: {} is odd but divisible by 4.'.format(num4))

    diversible(checkDiv, num2, num4)
    print('//////////////////////////')


def diversible(checkDiv, num2, num4):
    if checkDiv % 2 == 0:
        print(f'{checkDiv % 2 == 0} : {num2} divisible with {num4} is: {checkDiv} is an Even number.')
    elif checkDiv % 2 != 0:
        print(f'{checkDiv % 2 != 0} : {num2} divisible with {num4} is: {checkDiv} is an Odd number.')
    print('//////////////////////////')
    rerun()


game()
