import pandas as pd
import random

# 1 = pile1
# 2 = pile2
# 3 = pile3
# 4 = draftPool
# 5 = playerOnePool
# 6 = playerTwoPool
def replace_card(list_receiving, list_removing_number):
    match list_receiving:
        case 1:
            if draftPool == []:
                return
            pile1.append(draftPool.pop(0))
        case 2:
            if draftPool == []:
                return
            pile2.append(draftPool.pop(0))
        case 3:
            if draftPool == []:
                return
            pile3.append(draftPool.pop(0))
        case 5:
            match list_removing_number:
                case 1:
                    playerOnePool.append(pile1.pop(0))
                case 2:
                    playerOnePool.append(pile2.pop(0))
                case 3:
                    playerOnePool.append(pile3.pop(0))
        case 6:
            match list_removing_number:
                case 1:
                    playerTwoPool.append(pile1.pop(0))
                case 2:
                    playerTwoPool.append(pile2.pop(0))
                case 3:
                    playerTwoPool.append(pile3.pop(0))             
                    
def get_choice_input():
    choice = -1
    while choice not in (1, 2):
        choice = int(input("Take Pile (1)\nSkip Pile (2)\n$")) # type: ignore
    return choice

def process_choice(pile_num, player_choosing, choice):
    match choice:
        case 1:
            match player_choosing:
                case 1:
                    match pile_num:
                        case 1:
                            while pile1:
                                replace_card(5, 1)
                            replace_card(1, 4)
                        case 2:
                            while pile2:
                                replace_card(5, 2)
                            replace_card(2, 4)
                        case 3:
                            while pile3:
                                replace_card(5, 3)
                            replace_card(3, 4)
                case 2:
                    match pile_num:
                        case 1:
                            while pile1:
                                replace_card(6, 1)
                            replace_card(1, 4)
                        case 2:
                            while pile2:
                                replace_card(6, 2)
                            replace_card(2, 4)
                        case 3:
                            while pile3:
                                replace_card(6, 3)
                            replace_card(3, 4)
        case 2:
            match pile_num:
                case 1:
                    replace_card(1, 4)
                case 2:
                    replace_card(2, 4)
                case 3:
                    replace_card(3, 4)

def display_piles(pile_shown_num):
    print("Cards Remaining:",len(draftPool))
    print()
    match pile_shown_num:
        case 1:
            print("Pile 1:")
            for card in pile1:
                print(card)
            print()
            print("Pile 2:")
            print(len(pile2),"cards")
            print()
            print("Pile 3:")
            print(len(pile3),"cards")
            print()
        case 2:
            print("Pile 1:")
            print(len(pile1),"cards")
            print()
            print("Pile 2:")
            for card in pile2:
                print(card)
            print()
            print("Pile 3:")
            print(len(pile3),"cards")
            print()
        case 3:
            print("Pile 1:")
            print(len(pile1),"cards")
            print()
            print("Pile 2:")
            print(len(pile2),"cards")
            print()
            print("Pile 3:")
            for card in pile3:
                print(card)
            print()
            
done = False

draftPool = [None] * 90
playerOnePool = []
playerTwoPool = []

df = pd.read_csv('cardList.csv')

rows, columns = df.shape

random_choices = random.sample(range(0, rows), 90)

# data = df.iloc[0,0]

i = 0

while i < 90:
    draftPool[i] = df.iloc[random_choices[i],0] # type: ignore
    i = i + 1
    
pile1 = []
pile2 = []
pile3 = []

# put initial cards in each pile
pile1.append(draftPool.pop(0))
pile2.append(draftPool.pop(0))
pile3.append(draftPool.pop(0))

print("Winston Draft Starting!\n")

while done == False:
    print("Player 1")
    display_piles(1)
    choice = get_choice_input()  # type: ignore
    process_choice(1, 1, choice)
    if choice == 2:
        display_piles(2)
        choice = get_choice_input()  # type: ignore
        process_choice(2, 1, choice)
        if choice == 2:
            display_piles(3)
            choice = get_choice_input()  # type: ignore
            process_choice(3, 1, choice)
    print("Player 2")
    display_piles(1)
    choice = get_choice_input()  # type: ignore
    process_choice(1, 2, choice)
    if choice == 2:
        display_piles(2)
        choice = get_choice_input()  # type: ignore
        process_choice(2, 2, choice)
        if choice == 2:
            display_piles(3)
            choice = get_choice_input()  # type: ignore
            process_choice(3, 2, choice)
    if pile1 == [] and pile2 == [] and pile3 == []:
        done = True

playerOneDeck = open("playerOneDeck.txt", "w")
playerTwoDeck = open("playerTwoDeck.txt", "w")

for card in playerOnePool:
    playerOneDeck.write("1 " + card + "\n")
for card in playerTwoPool:
    playerTwoDeck.write("1 " + card + "\n")

playerOneDeck.close()
playerTwoDeck.close()
