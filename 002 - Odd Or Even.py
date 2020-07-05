import random
import sys


def rerun(seq, seq_no):
    """Asking if user wants to run again"""
    choice = input('Do you wanna rerun again?: <Y> Yes | <S> Sequence | <Any Key> Exit\n')
    choice = choice.upper()
    if choice == 'Y':
        game(seq, seq_no)
    elif choice == 'S':
        rerunTimes()
    else:
        sys.exit(0)


def rerunTimes():
    seq = int(input('How many times do you wanna run it?: '))
    seq_no = seq
    # print('Rerunning in 3')
    # time.sleep(1)
    # print('Rerunning in 2')
    # time.sleep(1)
    # print('Rerunning in 1')
    # time.sleep(1)
    game(seq, seq_no)


def game(seq=1, first_play=True):
    seq_no = 2
    while first_play:
        seq_no -= 1
        print('Total Number to reach', seq)
        print(f'Sequence Number: {seq_no}.')
        print(first_play)
        if first_play:
            first_play = False
            if seq == 1:
                """Automate that shit"""
                num2 = random.randint(1, 100)
                num4 = random.randint(1, 100)
                print(f'First random number is between 1 - 100\n1st number is: {num2}')
                print(f'Second random number is between 1 - 100\n2nd number is: {num4}')
                print('//////////////////////////')
                calc(num2, num4, seq, seq_no, first_play)
            elif seq_no >= seq:
                rerun(seq, seq_no)
    else:
        if seq_no > seq:
            """Automate that shit"""
            num2 = random.randint(1, 100)
            num4 = random.randint(1, 100)

            print(f'First random number is between 1 - 100\n1st number is: {num2}')
            print(f'Second random number is between 1 - 100\n2nd number is: {num4}')
            print('//////////////////////////')
            calc(num2, num4, seq, seq_no, first_play)
        elif seq_no == seq:
            rerun(seq, seq_no)


def calc(num2, num4, seq, seq_no, first_play):
    oddOrEvenNum2 = num2 % 2
    oddOrEvenNum4 = num4 % 2
    multipleOf4Num2 = num2 % 4
    multipleOf4Num4 = num4 % 4
    checkDiv = num2 % num4

    """TESTING"""
    print('::: Testing :::')
    print(num2 % 2, 'oddOrEvenNum2')
    print(num4 % 2, 'oddOrEvenNum4')
    print(multipleOf4Num2, 'multipleOf4Num2')
    print(multipleOf4Num4, 'multipleOf4Num4')
    print(checkDiv, 'checkDiv')
    print('//////////////////////////')

    prints(oddOrEvenNum2, oddOrEvenNum4, multipleOf4Num2, multipleOf4Num4, checkDiv, num2, num4, seq, seq_no,
           first_play)


def prints(oddOrEvenNum2, oddOrEvenNum4, multipleOf4Num2, multipleOf4Num4, checkDiv, num2, num4, seq, seq_no,
           first_play):
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

    diversible(checkDiv, num2, num4, seq, seq_no, first_play)
    print('//////////////////////////')


def diversible(checkDiv, num2, num4, seq, seq_no, first_play):
    if checkDiv % 2 == 0:
        print(f'{checkDiv % 2 == 0} : {num2} divisible with {num4} is: {checkDiv} is an Even number.')
    elif checkDiv % 2 != 0:
        print(f'{checkDiv % 2 != 0} : {num2} divisible with {num4} is: {checkDiv} is an Odd number.')

    if first_play:
        if seq_no > 0:
            game(seq, seq_no, first_play)
        else:
            rerun(seq, seq_no)


game(seq=1)