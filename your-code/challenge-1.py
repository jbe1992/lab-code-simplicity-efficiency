"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('''Welcome to this calculator!
      It can add and subtract whole numbers from zero to five''')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')

check_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'plus', 'minus']
sum_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', -1: 'negative one', -2: 'negative two',
            -3: 'negative three', -4: 'negative four', -5: 'negative five'}


def calculate(number1,operator,number2):
    if operator == 'plus':
        if sum_dict[number1] + sum_dict[number2] > 5:
            result = sum_dict[sum_dict[number1] + sum_dict[number2]]
        else:
            result = sum_dict[sum_dict[number1] + sum_dict[number2]]
    elif operator == 'minus':
        if sum_dict[number1] < sum_dict[number2]:
            result = sum_dict[sum_dict[number1] - sum_dict[number2]]
        else:
            result = sum_dict[sum_dict[number1] - sum_dict[number2]]
    else:
        print('Error. You should select a correct operator.')
    print(f'{number1} {operator} {number2} equals {result}')


if (a not in check_list) or (b not in check_list) or (c not in check_list):
    print("I am not able to answer this question. Check your input.")
else:
    calculate(a, b, c)
print("Thanks for using this calculator, goodbye :)")
