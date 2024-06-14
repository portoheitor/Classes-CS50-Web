number = input("Number: ")
number_int = int(number)

if number_int > 0:
    print(f'{number_int} is Positive!')
elif number_int < 0:
    print(f'{number_int} is Negative!')
else:
    print(f'{number_int} is Zero!')