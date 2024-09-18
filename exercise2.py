import random

number_random=random.randint(1, 100)
print(f"Computer lottery{number_random}")

while True:
    number_guss: int = int(input("what is your number?"))
    if number_guss == number_random:
        print('bingo')
        break
    elif number_random > number_guss:
        print('Your number is too small')
    else:
        print('Your number is too big')

