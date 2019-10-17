# Write a function called choose_func which takes a list of nums and 2
# callback functions. If all nums inside the list are positive, execute the
# first function on that list and return the result of it. Otherwise return the
# result of the second one


def choose_func(nums: list, func1, func2):

    if len(func2(nums)) < len(nums):
        return func2(nums)

    return func1(nums)


# Assertions
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

# Implement a simple composition of 4 classes: ATM, Client, Card, Bank
#
# Bank(name) + accounts = [] - list of all accounts opened in the current bank
# methods:
#   open_account(client: Client) - takes an instance of Client class as an
# argument and creates a new instance of Card bound to this client (and returns
# it). ! A client can only open one account per bank !
#   close_account(card: Card) - removes specified instance of Card
#
# ATM(bank: Bank, amount: float) - takes an instance of Bank class as an
# argument (the bank this card is bound to) and the amount of money in
# the current ATM.
# methods:
#   withdraw(card: Card, sum: float) - takes two arguments: an instance of
# Card and sum which is needed to be withdrawn. You should consider 2 cases:
#       1) when the amount of money in the bank is less than the sum
#       2) when the ATM and Card are bound to different banks (it shouldn't
# let you withdraw)
#   add(card: Card, sum: float) - add the specified amount of money to the card
#   change_pin(card: Card, old_pin: int, new_pin: int) - change card's pin
#
# Card(account: int, balance: float, pin: int, owner: Client, bank: Bank) -
# account is just a random 5-digit number. Pin is 0000 by default
# methods:
#   transfer_money(card, amount) - transfers the money from the current card to
# the specified one
#
# Client(name: str) + cards = [] - list of cards bound to the client
# methods:
#   show_total_balance - returns the sum of money from all cards owned by the
# client


class Bank:

    def __init__(self, name, accounts=None):
        self.name = name
        self.accounts = accounts or []

    def open_account(self, client, bank, account):
        if set(client.cards).isdisjoint(set(bank.accounts)):
            new_account = Card(account, client, bank)
            self.accounts.append(new_account)
            Client.add_card(client, new_account)
            return new_account
        else:
            print('Account already exists')

    def close_account(self, card):
        self.accounts.remove(card)


class ATM:

    def __init__(self, bank, sum=0):
        self.bank = bank
        self.sum = float(sum)

    def add(self, card, sum):
        card.balance += sum

    def withdraw(self, card, sum):
        if self.bank.name != card.bank.name:
            print('Sorry, this card is out of service')
        elif self.sum < sum:
            print('ATM insufficient funds')
        else:
            card.balance -= sum

    def change_pin(self, card, old_pin, new_pin):
        if card.pin == old_pin:
            card.pin = new_pin
        else:
            print('Pin is wrong')


class Card:

    def __init__(self, account, owner, bank, balance=0,  pin='0000'):
        self.account = int(account)
        self.balance = float(balance)
        self.bank = bank
        self.pin = pin
        self.owner = owner


    def transfer_money(self, card, amount):
        if self.balance < amount:
            print('Insufficient funds')
        else:
            self.balance -= float(amount)
            card.balance += float(amount)

    def __repr__(self):
        return str(self.account)        # to return a list of accs in bank

class Client:

    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards or []


    def show_total_balance(self):
        return sum([sum.balance for sum in self.cards])

    #   show_total_balance - returns the sum of money from all cards owned by the
    # client

    def add_card(self, card):      # additional method to add cards to a client's
        self.cards.append(card)    # cards list



bank1 = Bank("PrivatBank")
bank2 = Bank('Monobank')

client1 = Client("John")
client2 = Client('Steve')

atm1 = ATM(bank1, 10000)
atm2 = ATM(bank2, 5000)

john_card1 = bank1.open_account(client1, bank1, 10010)
john_card2 = bank2.open_account(client1, bank2, 20010)

steve_card1 = bank1.open_account(client2, bank1, 10020)
steve_card2 = bank2.open_account(client2, bank2, 20020)


print('\nDuplicate account check:')
print(john_card1.account)
print(john_card2.account)

print(steve_card1.account)
print(steve_card2.account)

john_card3 = bank1.open_account(client1, bank1, 10030)
steve_card3 = bank2.open_account(client2, bank2, 20030)

print(john_card1.account)
print(john_card2.account)

print(steve_card1.account)
print(steve_card2.account)

print('\nChech add and withdraw methods:')
print(john_card1.balance)
print(steve_card2.balance)

atm1.add(john_card1, 1000)
atm2.add(steve_card2, 2000)

print('\nDeposit result:')

print(john_card1.balance)
print(steve_card2.balance)

atm1.withdraw(john_card1, 15000)
atm1.withdraw(steve_card2, 430.55)
atm2.withdraw(steve_card2, 430.55)

print('\nWithdrawal result:')
print(john_card1.balance)
print(steve_card2.balance)

print('\nPin change:')
print(john_card1.pin)

atm1.change_pin(john_card1, '1111', '2222')
atm1.change_pin(john_card1, '0000', '0022')

print(john_card1.pin)

print('\nTransfer money check:')
print(john_card1.balance)
print(steve_card2.balance)

john_card1.transfer_money(steve_card2, 1500)
john_card1.transfer_money(steve_card2, 500)

print(john_card1.balance)
print(steve_card2.balance)

print('\nClose account check:')
print(f"Bank accounts: {bank1.accounts}")
print(f"Client1 cards: {client1.cards}")
bank1.close_account(john_card1)
print(f"Bank accounts: {bank1.accounts}")
print(f"Client1 cards: {client1.cards}")

print(client2.show_total_balance())

