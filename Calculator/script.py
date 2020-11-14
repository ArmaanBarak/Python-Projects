# This calculator is able to calculate repeatedly

# counter to check if its the first number user is entering
iterations = 0

# getting user input
def input_num():
    '''
    This function is used to input numbers.
    It is made to ensure that user only inputs numbers.

    The input text is kept different for first iteration 
    and all subsequent iterations.
    '''
    while True:
        try:
            if iterations == 0:
                num = float(input('Please Enter your first number (Digits):\n>>> '))
            else:
                num = float(input('>>> '))
            break
        except:
            print('Please enter only digits. Retry:\n')

    return num

def main(num1, oper):
    '''
    Main function used to perform calculations and
    keep track of numbers.

    Returns a tuple of first number and number of iterations.
    '''
    global iterations
    iterations += 1

    if oper == '+':
        print(f'Add {num1} to:')
        num2 = input_num()
        num1 += num2
        print('>>>', num1)
    
    elif oper == '-':
        print(f'Subtract {num1} from:')
        num2 = input_num()
        num1 = num2 - num1
        print('>>>', num1)

    elif oper == '*':
        print(f'Multiply {num1} with:')
        num2 = input_num()
        num1 *= num2
        print('>>>', num1)

    elif oper == '/':
        print(f'Divide {num1} by:')
        num2 = input_num()
        try:
            num1 /= num2
        except ZeroDivisionError:
            print('>>> Undefined!')
    
    elif oper == '%':
        print(f'Remainder of {num1} when divided by:')
        num2 = input_num()
        try:
            num1 %= num2
        except ZeroDivisionError:
            print('>>> Undefined!')

    elif oper == '//':
        print(f'Floor Division of {num1} by:')
        num2 = input_num()
        try:
            num1 //= num2
        except ZeroDivisionError:
            print('>>> Undefined!')

    elif oper == '**':
        print(f'{num1} raised to power of:')
        num2 = input_num()
        num1 **= num2
        print('>>>', num1)
    
    elif oper.lower() == 'quit':
        quit()

    else:
        print('Sorry! You didn\'t gave a recognizable input.')

    return (num1, iterations)

if __name__ == "__main__":

    num1 = input_num()

    while True:
        
        if iterations == 0:
            oper = input('Enter an operator: (+, -, *, /, %, **, //)\nType quit to exit the calculator\n>>> ')
            print()
        else:
            print()
            print('New Number:', num1, '\n')
            oper = input('Enter an operator: (+, -, *, /, %, **, //)\nType quit to exit the calculator\n>>> ')
            print()

        num1, iterations = main(num1, oper)
