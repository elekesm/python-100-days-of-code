auction = {}

while True:
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_bidders == "yes":
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        auction[name] = bid
        print("\n" * 3)
    else:
        break

highest_bidder = ""
highest_bid = 0

for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = auction[bidder]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")