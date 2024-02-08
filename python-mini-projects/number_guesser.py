import random
'''
#deon't include -5 and 10 in random number
r=random.randrange(-5 ,10)
print(r)


#includes -5 and 11 in random numbers
r=random.randint(-5 ,10)
print(r)

'''
top_of_range = input('type a number:  ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print(' please type a number larger than zero next time!')
        quit()
else:
    print('please type a number next time.')
    quit()


#include numbers from 0 to top_of_range
random_number = random.randint(0,top_of_range)
#print('RANDOM NUMBER IS :'+ str(random_number))

while True:

    user_guess= input('Now Guess a number : ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == random_number:
        print('HUrray, you got it correct! ')
        break

    else:
        print('Sorry,you got it wrong! :( ')
        print('RANDOM NUMBER was actually  :',(random_number)) # 'text'+str(random_number) is same as 'text',random_number

