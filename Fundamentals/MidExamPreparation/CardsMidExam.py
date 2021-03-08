cards = input().split(":")
deck = []
line = input()


def card_name_in_cards(card, cards):
    if card in cards:
        return True


def index_in_range(index, cards):
    if 0 <= index < len(cards):
        return True


while line != "Ready":
    command, *value = line.split()
    if command == "Add":
        card_name = value[0]
        if card_name_in_cards(card_name, cards):
            deck.append(card_name)
        else:
            print("Card not found.")

    elif command == "Insert":
        card_name = value[0]
        index = int(value[1])
        if card_name_in_cards(card_name, cards) and index_in_range(index, cards):
            deck.insert(index, card_name)
        else:
            print("Error!")


    elif command == "Remove":
        card_name = value[0]
        if card_name_in_cards(card_name, deck):
            deck=[x for x in deck if x!=card_name]
            # deck.remove(card_name)
        else:
            print("Card not found.")

    elif command == "Swap":
        card_name_one = value[0]
        card_name_two = value[1]
        index_one=deck.index(card_name_one)
        index_two=deck.index(card_name_two)
        deck.remove(card_name_two)
        deck.remove(card_name_one)
        deck.insert(index_one,card_name_two)
        deck.insert(index_two,card_name_one)

    elif command == "Shuffle":
        deck=reversed(deck)

    line = input()

print(" ".join(deck))
