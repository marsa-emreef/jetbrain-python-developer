# Write your code here
from math import floor


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")


def process_buy(water, milk, coffee,
                disposable_cups, money, coffee_machine):
    enough_water = coffee_machine.water >= water
    enough_milk = coffee_machine.milk >= milk
    enough_coffee = coffee_machine.coffee >= coffee
    enough_cups = coffee_machine.cups >= disposable_cups

    out_ouf_resource = []
    if not enough_water:
        out_ouf_resource.append('water')
    elif not enough_milk:
        out_ouf_resource.append('milk')
    elif not enough_coffee:
        out_ouf_resource.append('coffee')
    elif not enough_cups:
        out_ouf_resource.append('cups')

    if len(out_ouf_resource) == 0:
        print("I have enough resources, making you a coffee!")
        coffee_machine.water = coffee_machine.water - water
        coffee_machine.milk = coffee_machine.milk - milk
        coffee_machine.coffee = coffee_machine.coffee - coffee
        coffee_machine.cups = coffee_machine.cups - disposable_cups
        coffee_machine.money = coffee_machine.money + money
    else:
        print('Sorry, not enough ' + ','.join(out_ouf_resource) + '! ')


def buy_cappuccino(coffee_machine):
    water = 200
    milk = 100
    coffee_beans = 12
    disposable_cups = 1
    money = 6
    return process_buy(water, milk, coffee_beans, disposable_cups, money, coffee_machine)


def buy_latte(coffee_machine):
    water = 350
    milk = 75
    coffee_beans = 20
    disposable_cups = 1
    money = 7
    return process_buy(water, milk, coffee_beans, disposable_cups, money, coffee_machine)


def buy_espresso(coffee_machine):
    water = 250
    milk = 0
    coffee_beans = 16
    disposable_cups = 1
    money = 4
    return process_buy(water, milk, coffee_beans, disposable_cups, money, coffee_machine)


def do_buy(coffee_to_buy, coffee_machine):
    if coffee_to_buy == '3':
        buy_cappuccino(coffee_machine)
    elif coffee_to_buy == '2':
        buy_latte(coffee_machine)
    elif coffee_to_buy == '1':
        buy_espresso(coffee_machine)
    else:
        print('Sorry, wrong selection.')


def perform_fill(coffee_machine):
    water_to_add = int(input('Write how many ml of water do you want to add:'))
    milk_to_add = int(input('Write how many ml of milk do you want to add:'))
    coffee_to_add = int(input('Write how many grams of coffee beans do you want to add:'))
    cups_to_add = int(input('Write how many disposable cups of coffee do you want to add:'))
    coffee_machine.water = coffee_machine.water + water_to_add
    coffee_machine.milk = coffee_machine.milk + milk_to_add
    coffee_machine.coffee = coffee_machine.coffee + coffee_to_add
    coffee_machine.cups = coffee_machine.cups + cups_to_add


def perform_take(coffee_machine):
    print(f'I gave you ${coffee_machine.money}')
    coffee_machine.money = 0


def perform_action(coffee_machine):
    action = input("Write action (buy, fill, take, remaining, exit):")
    if action == "buy":
        coffee_to_buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        do_buy(coffee_to_buy, coffee_machine)
    elif action == "fill":
        perform_fill(coffee_machine)
    elif action == "take":
        perform_take(coffee_machine)
    elif action == "remaining":
        coffee_machine.print_state()
    elif action == "exit":
        return
    perform_action(coffee_machine)


perform_action(CoffeeMachine())
