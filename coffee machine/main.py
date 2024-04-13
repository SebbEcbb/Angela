import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

payments = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
    "total": 0,
}


def make_espresso():
    # gather information
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    milk = 0
    cost = float(MENU["espresso"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    print("-----------------\n")

    print(f"Your drink is being prepared.\n")

    print(f"Your drink is ready. Thank you!")

    update_resources(water, coffee, milk)

    new_order()


def make_latte():
   # gather information
    water = MENU["latte"]["ingredients"]["water"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    milk = MENU["latte"]["ingredients"]["milk"]
    cost = float(MENU["latte"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    print("-----------------\n")

    print(f"Your drink is being prepared.\n")

    print(f"Your drink is ready. Thank you!")

    update_resources(water, coffee, milk)

    new_order()


def make_cappuccino():
    # gather information
    water = MENU["cappuccino"]["ingredients"]["water"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    cost = float(MENU["cappuccino"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    print("-----------------\n")

    print(f"Your drink is being prepared.\n")

    print(f"Your drink is ready. Thank you!")

    update_resources(water, coffee, milk)

    new_order()


def print_report():
    print("-----------------------")
    print(f"Water: {resources["water"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Mik: {resources["milk"]}\n")
    print("-----------------------")
    print(f"Quarters: {payments["quarters"]}")
    print(f"Dimes: {payments["dimes"]}")
    print(f"Nickels: {payments["nickles"]}")
    print(f"Pennies: {payments["pennies"]}")
    print(f"Total: {payments["total"]}")
    print("-----------------------")
    new_order()


def new_order():
    # Get customers order
    choice = input("What would you like? (enter: 'e' or 'espresso'/'l' or 'latte'/ 'c' or 'cappuccino'):\n")

    if choice == "e" or choice == "espresso":
        print("You chose espresso.")
        make_espresso()
    elif choice == "l" or choice == "latte":
        print("You chose latte.")
        make_latte()
    elif choice == "c" or choice == "cappuccino":
        print("You chose cappuccino.")
        make_cappuccino()
    elif choice == "report":
        print("You select report.")
        print_report()
    elif choice == "off":
        print("Machine shutting down. Thank you and bye bye!")
        sys.exit()
    else:
        print('Please enter a valid command.')
        new_order()


def check_resources(water, coffee, milk):
    if resources["water"] - water <= 0:
        end()
    elif resources["coffee"] - coffee <= 0:
        end()
    elif resources["milk"] - milk <= 0:
        end()


def end():
    print(f"Sorry the machine is empty. Chose another drink.")
    new_order()


def pay(cost):
    print(f' Costs: {cost}. Please enter you payment')
    paid = 0
    while paid < cost:
        coin = input("Please insert a coin :type  'q' for quarter, 'd' for dimes, 'n' for nickel and 'p' for penny :")

        if coin == "q":
            payments["quarters"] += 1
            paid += 0.25
            print(f"remaining : {cost - paid}.")

        if coin == "d":
            payments["dimes"] += 1
            paid += 0.10
            print(f"remaining : {cost - paid}.")

        if coin == "n":
            payments["nickles"] += 1
            paid += 0.05
            print(f"remaining : {cost - paid}.")

        if coin == "p":
            payments["pennies"] += 1
            paid += 0.01
            print(f"remaining : {cost - paid}.")

    if paid > cost:
        change = round(paid - cost, 2)
        print(f"You paid $ {paid}")
        print(f"Your change is {change}.")

    payments["total"] += cost


def update_resources(water, coffee, milk):
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk


# Start machine here
new_order()