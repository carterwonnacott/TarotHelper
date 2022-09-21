import json
import random

DECKS_KEY = "decks"
DECK_NAME_KEY = "deckName"
DECK_DESC_KEY = "deckDesc"
DECK_CARDS_KEY = "deckCards"
CARD_NAME_KEY = "cardName"
CARD_MEANING_KEY = "cardMeaning"
CARD_INVERSE_MEANING_KEY = "cardInverseMeaning"

while (1):
    print("\nWelcome to the Tarot card shuffler! Would you like to:")
    print("1. Draw from an existing tarot deck")
    print("2. Create a new tarot deck")
    print("3. Edit an existing deck")
    print("4. Delete an existing deck")
    print("x. Exit")
    select = input()

    with open('decks.json', 'r') as openfile:
        decks = json.load(openfile)

    #Draw from an existing Tarot deck
    if (select == "1"):
        print("Please provide the name of the deck you would like to draw from:")
        deckName = input()
        res = list(filter(lambda i: i[DECK_NAME_KEY] == deckName, decks[DECKS_KEY]))
        if len(res) == 0:
            print("Please provide a valid name.")
            continue
        deck = res[0]
        random.shuffle(deck[DECK_CARDS_KEY])
        invIndexes = []
        while len(invIndexes) < len(deck[DECK_CARDS_KEY])/2:
            i = random.randint(0, len(deck[DECK_CARDS_KEY]) - 1)
            if i not in invIndexes:
                invIndexes.append(i)

        while (1):
            print("Please enter a card number, or 'x' to exit:")
            cardNum = input()
            if cardNum == "x":
                break
            i = int(cardNum)
            if i < 0 or i >= len(deck[DECK_CARDS_KEY]):
                print("Please use a valid number. The deck has %d cards." % len(deck[DECK_CARDS_KEY]))
                continue
            
            if i in invIndexes:
                print("REVERSED")
            print(json.dumps(deck[DECK_CARDS_KEY][i], indent=2))
            

    #Create a new tarot deck
    elif (select == "2"):
        print("What would you like the name of this new deck to be?")
        deckName = input()
        deck = {}
        deck[DECK_NAME_KEY] = deckName
        print("Please provide a description for this deck:")
        deckDesc = input()
        deck[DECK_DESC_KEY] = deckDesc
        print("How many cards will be in this deck?")
        numCards = int(input())

        deck[DECK_CARDS_KEY] = []
        for i in range(numCards):
            newCard = {}
            print("What will be the name of card #%s?" % i)
            cardName = input()
            newCard[CARD_NAME_KEY] = cardName
            print("What is the meaning of card #%s?" % i)
            cardMeaning = input()
            newCard[CARD_MEANING_KEY] = cardMeaning
            print("What is the meaning of card #%s when inverted?" % i)
            cardInverseMeaning = input()
            newCard[CARD_INVERSE_MEANING_KEY] = cardInverseMeaning
            deck[DECK_CARDS_KEY].append(newCard)
        
        # add deck to decks
        decks[DECKS_KEY].append(deck)
        with open("decks.json", "w") as outfile:
            outfile.write(json.dumps(decks))

    # edit an existing deck
    elif (select == "3"):
        edited = False
        print("Please provide the name of the deck you would like to edit:")
        deckName = input()
        res = list(filter(lambda i: i[DECK_NAME_KEY] == deckName, decks[DECKS_KEY]))
        if len(res) == 0:
            print("Please provide a valid name.")
            continue
        deck = res[0]
        while (1):
            print("Here is the deck:")
            print(json.dumps(deck, indent=2))
            print("What would you like to edit?")
            print("1. Name")
            print("2. Description")
            print("3. Cards")
            print("x. Exit")
            option = input()

            if option == "1":
                print("Please enter new deck name:")
                deck[DECK_NAME_KEY] = input()
                decks[DECKS_KEY] = list(filter(lambda i: i[DECK_NAME_KEY] != deck[DECK_NAME_KEY], decks[DECKS_KEY]))
                decks[DECKS_KEY].append(deck)
                edited = True

            
            elif option == "2":
                print("Please enter new deck description:")
                deck[DECK_DESC_KEY] = input()
                decks[DECKS_KEY] = list(filter(lambda i: i[DECK_NAME_KEY] != deck[DECK_NAME_KEY], decks[DECKS_KEY]))
                decks[DECKS_KEY].append(deck)
                edited = True


            elif option == "3":
                print("Please enter the name of the card you would like to edit or add to this deck:")
                cardName = input()
                res = list(filter(lambda i: i[CARD_NAME_KEY] == cardName, deck[DECK_CARDS_KEY]))
                if len(res) == 0:
                    print("There is no card in this deck with that name. Input \"y\" to add a card with that name into the deck:")
                    response = input()
                    if (response == "y"):
                        newCard = {}
                        newCard[CARD_NAME_KEY] = cardName
                        print("What is the meaning of card #%s?" % i)
                        cardMeaning = input()
                        newCard[CARD_MEANING_KEY] = cardMeaning
                        print("What is the meaning of card #%s when inverted?" % i)
                        cardInverseMeaning = input()
                        newCard[CARD_INVERSE_MEANING_KEY] = cardInverseMeaning
                        deck[DECK_CARDS_KEY].append(newCard)
                        decks[DECKS_KEY] = list(filter(lambda i: i[DECK_NAME_KEY] != deck[DECK_NAME_KEY], decks[DECKS_KEY]))
                        decks[DECKS_KEY].append(deck)
                        edited = True
                    continue

                card = res[0]
                print("Here is the card:")
                print(json.dumps(card, indent=2))
                print("What would you like to edit?")
                print("1. Name")
                print("2. Meaning")
                print("3. Inverse Meaning")
                print("4. Delete Card")
                print("x. Exit")
                option = input()

                if option == "1":
                    print("Please enter new card name:")
                    card[CARD_NAME_KEY] = input()
                    deck[DECK_CARDS_KEY] = list(filter(lambda i: i[CARD_NAME_KEY] != card[CARD_NAME_KEY], deck[DECK_CARDS_KEY]))
                    deck[DECK_CARDS_KEY].append(card)
                    edited = True

                elif option == "2":
                    print("Please enter new card meaning:")
                    card[CARD_MEANING_KEY] = input()
                    deck[DECK_CARDS_KEY] = list(filter(lambda i: i[CARD_NAME_KEY] != card[CARD_NAME_KEY], deck[DECK_CARDS_KEY]))
                    deck[DECK_CARDS_KEY].append(card)
                    edited = True

                elif option == "3":
                    print("Please enter new card inverse meaning:")
                    card[CARD_INVERSE_MEANING_KEY] = input()
                    deck[DECK_CARDS_KEY] = list(filter(lambda i: i[CARD_NAME_KEY] != card[CARD_NAME_KEY], deck[DECK_CARDS_KEY]))
                    deck[DECK_CARDS_KEY].append(card)
                    edited = True

                elif option == "4":
                    deck[DECK_CARDS_KEY] = list(filter(lambda i: i[CARD_NAME_KEY] != card[CARD_NAME_KEY], deck[DECK_CARDS_KEY]))
                    edited = True
                
                elif option == "x":
                    continue

                else:
                    print("Please provide valid input.")
                
                if edited:
                    decks[DECKS_KEY] = list(filter(lambda i: i[DECK_NAME_KEY] != deck[DECK_NAME_KEY], decks[DECKS_KEY]))
                    decks[DECKS_KEY].append(deck)
            
            elif option == "x":
                break

            else:
                print("Please provide a valid input.")

        if edited:    
            with open("decks.json", "w") as outfile:
                outfile.write(json.dumps(decks))


    # delete an existing deck
    elif (select == "4"):
        print("Which deck would you like to delete?")
        deckToDeleteName = input()
        if (deckToDeleteName == ""):
            continue
        decks[DECKS_KEY] = list(filter(lambda i: i[DECK_NAME_KEY] != deckToDeleteName, decks[DECKS_KEY]))
        with open("decks.json", "w") as outfile:
            outfile.write(json.dumps(decks))

    # exit the program
    elif (select == "x"):
        break

    # invalid input
    else:
        print("Please provide valid input.")