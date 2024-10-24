import random
number=random.randint(0,10)
while True:
    ask=int(input('enter a number'))
    if number==ask:
        break
    elif number>ask:
        print('too low')
    elif number<ask:
        print('too high')