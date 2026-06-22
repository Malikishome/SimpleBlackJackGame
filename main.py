# This is my 1st code that i wrote on my owm

import random # random cards
import time # slow down the comp
cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] # the deck of cards
target = 21

def pickacard():
    yourScore = 0 #init the score
    while True: # this is a loop that keeps running forever — until we manually tell it to stop using a break statement.
        ans = input("Do you want to hit? y or n: ").lower()
        if ans == 'y':
            cardspicked = random.choice(cards) # choose a random card from the list
            yourScore += cardspicked # add that card to out score
            print(f'your picked up {cardspicked} so you now have {yourScore}')
            if yourScore > target:
                print('you bust', yourScore)
                break
        elif ans == 'n': # we pick no and we get out of the look and its the comp's turn
            break
    return yourScore

finalScore = pickacard()

if finalScore == target:
    print('BlackJack :)', finalScore)

def compCard(): # comp side
    compScore = 0 # init the score
    while compScore < 17: # This is telling teh comp to keep going until it reaches a valid point to stop to make the game fun
        time.sleep(2) # slow down the comp
        comppickedcard = random.choice(cards)
        compScore += comppickedcard
        print(f'we picked {comppickedcard} so we got {compScore}')

    return compScore

compFinalScore = compCard()
if compFinalScore == target:
    print('We got BlackJack', compFinalScore)
elif compFinalScore > target:
    print('Damn the comp Bust', compFinalScore)
else:
    print(compFinalScore)


print(f'Our score was {finalScore} and the comp score was {compFinalScore}')


