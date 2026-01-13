import random
from collections import Counter

someWords = '''apple banan mango strawberry grape orange pineapple apricot lemon watermelon cherry peach'''
someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! Hint: its a fruit')

    for i in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 3
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter on a Letter')
                continue
            elif len(guess) > 1:
                print('Enter only a single letter')
                continue
            elif guess in letterGuessed:
                print(f'You have aleady guessed letter: {guess}')
                continue

            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Cograts, you won!")
                    break
                    break
                else:
                    print('_', end=' ')
        
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! try again...')
            print('The word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye!')
        exit()
