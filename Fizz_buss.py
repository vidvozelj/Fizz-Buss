while True:
    user_input = input('Eneter a number beetween 1-100: ')
    if user_input.isdigit():
        if int(user_input) > 100:
            print('You entered to large number!!')
        else:
            break
    else:
        print('Input is not a digit')

number = int(user_input)
 
for _ in range(1, number):
    if _ % 3 ==0 and _ % 5 ==0:
        print('Fizz-Buss')
    elif _ % 3 ==0:
        print('Fizz')
    elif _ % 5 ==0:
        print('Buss')
    else:
        print(_)