#HigherOrLower

import random

# Card Constant

SUIT_TUPLE = ( 'Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ( 'Ace', '2', '3', '4', '5', '6', '7' , '8', '9', 'Jack', 'Queen', 'King')

NCARDS = 8 

#Pass in a deck and this function returns a random card from the deck 
def getCard(deckListIn):
    thisCard = deckListIn.pop() #pop one off the top of the deck and return
    return thisCard

#Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() #Make of copy of deck list in
    random.shuffle(deckListOut)
    return deckListOut

# Main Code
print('\n')
print('Welcome to Higher or Lower.')
print('You have to choose wheather the next card is higher or lower than the current card')
print('Getting it right adds 20 points, Get it wrong and you lose 15 points')
print('You have 50 points to start')
print()

startingDeckList = []
for suit in SUIT_TUPLE:                                                         #1
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)


score = 50

while True:     # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)                                        #2
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit )
    print()


    for cardNumber in range(0, NCARDS): #play one game of this many cards           #3
        answer = input('Will the next card be higher or lower than the ' +
                        currentCardRank + ' of ' +
                        currentCardSuit + '? (enter h or l): ') 
        answer = answer.casefold() #force lower case
        nextCardDict = getCard(gameDeckList)                                        #4
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Next Card is:' , nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':                                                            #5
            if nextCardValue > currentCardValue:
                print('You got it Right, It was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')
            else:
                score = score - 15 
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue #dont need current suit
        currentCardSuit = nextCardSuit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')             #6
    if goAgain == 'q':
         break

print('Ok bye')