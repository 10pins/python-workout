### EXERCISE 1 - Number guessing game ###
import random

def guessing_game():
    guessed = False
    rand_num = random.randint(0,100)
    print('Random Number Generated.')

    while not guessed: 

        input_num = int(input('Guess the Random Number: '))

        if input_num == rand_num:
            print('Just right!')
            guessed = True
        elif input_num > rand_num:
            print('Too High!')
        else: 
            print('Too Low!')

    print(f'The number was {rand_num}')

    
if __name__ == '__main__':
    guessing_game()