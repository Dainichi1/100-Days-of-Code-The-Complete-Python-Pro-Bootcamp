# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
bidding = {}

name = input("What is your name? ")
bid = int(input("What is your bid?: $"))
bidding [name] = bid

repeat = input("Are there any other bitters? Type 'yes' or 'no'. ")
while repeat == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    bidding[name] = bid
    repeat = input("Are there any other bitters? Type 'yes' or 'no'. ")

print(bidding)
max_value = max(bidding.values())
for key in bidding:
    if bidding[key] == max_value:
        print(f"The winner is {key} with the amount of {bidding[key]}$")

