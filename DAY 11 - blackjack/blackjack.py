import random

# Deck of cards represented as a list of dictionaries, each with a rank and suit
french_deck = [
    {"rank": rank, "suit": suit}
    for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
    for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
]
random.shuffle(french_deck)

# Function to calculate the value of a card based on its rank and the current total
def card_value(card_rank: str, current_total: int) -> int:
    if card_rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        return int(card_rank)
    if card_rank in ["J", "Q", "K"]:
        return 10
    return 11 if current_total <= 10 else 1


def draw_cards(name: str, deck: list[dict], total: int = 0, continue_drawing=None) -> int:
    while total < 21:
        card = deck.pop(0)
        total += card_value(card["rank"], total)
        print(f"{name} drew {card['rank']} of {card['suit']}. {name}'s total is now {total}.")

        if total >= 21:
            break
        if continue_drawing is None:
            break
        if not continue_drawing(total):
            break
    return total


def player_wants_more(current_total: int) -> bool:
    return input("Do you want to draw another card? (y/n): ").strip().lower() == "y"


def dealer_wants_more(current_total: int) -> bool:
    return current_total < 16


player_total = draw_cards("Player", french_deck, total=0, continue_drawing=player_wants_more)
if player_total > 21:
    print("You bust!")
else:
    print(f"Your total is {player_total}.")

    dealer_total = draw_cards("Dealer", french_deck, total=0, continue_drawing=dealer_wants_more)
    if dealer_total > 21:
        print("Dealer busts!")
    else:
        print(f"Dealer's total is {dealer_total}.")
