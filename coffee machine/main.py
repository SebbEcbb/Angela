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
    "dollars": 0,
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
    "total": 0,
}


def make_espresso():
    print("-----------------\n")
    print("You chose espresso.")
    # gather information
    water = MENU["espresso"]["ingredients"]["water"]
    coffee = MENU["espresso"]["ingredients"]["coffee"]
    milk = 0
    cost = float(MENU["espresso"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    process(water, coffee, milk)


def make_latte():
    print("-----------------\n")
    print("You chose latte.")
    # gather information
    water = MENU["latte"]["ingredients"]["water"]
    coffee = MENU["latte"]["ingredients"]["coffee"]
    milk = MENU["latte"]["ingredients"]["milk"]
    cost = float(MENU["latte"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    process(water, coffee, milk)


def make_cappuccino():
    # gather information
    water = MENU["cappuccino"]["ingredients"]["water"]
    coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    milk = MENU["cappuccino"]["ingredients"]["milk"]
    cost = float(MENU["cappuccino"]["cost"])

    # Check if there are enough resources in the machine
    check_resources(water, coffee, milk)

    pay(cost)

    process(water, coffee, milk)


def process(water, coffee, milk):
    print("-----------------\n")

    print(f"Drink is being prepared.\n")

    print(f"Drink is ready. Thank you!")

    update_resources(water, coffee, milk)

    new_order()


def print_report():
    print("-----------------------")
    print(f"Water: {resources["water"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Milk: {resources["milk"]}\n")
    print("-----------------------")
    print(f"Dollars: {payments["dollars"]}")
    print(f"Quarters: {payments["quarters"]}")
    print(f"Dimes: {payments["dimes"]}")
    print(f"Nickels: {payments["nickles"]}")
    print(f"Pennies: {payments["pennies"]}")
    print(f"Total: {payments["total"]}")
    print("-----------------------")
    new_order()


def new_order():
    # Get customers order
    e = "'e' for espresso\n"
    t = "'l' for latte\n"
    c = "'c' for cappuccino\n"
    a = "'a' for admin. Requires password.\n"

    choice = input(f"Please make your choice? \n {e} {t} {c} {a}")

    if choice == "e" or choice == "espresso":
        make_espresso()
    elif choice == "l" or choice == "latte":
        make_latte()
    elif choice == "c" or choice == "cappuccino":
        print("You chose cappuccino.")
        make_cappuccino()
    elif choice == "a":
        admin()
    else:
        print('Please enter a valid command.')
        new_order()


def admin():

    password = "coffee"
    pw = input("Enter your password\n")
    if pw == "exit":
        new_order()
    elif pw == password:
        admin_choice = input("'r' for report\n'f' for fill\n'o' for machine off.\n")
        if admin_choice == "r":
            print("Print a report.")
            print_report()
        elif admin_choice == "f":
            print("Fill machine.")
            fill()
        elif admin_choice == "o":
            print("Machine is shutting down. Thank you and bye bye!")
            sys.exit()
    else:
        print("Please try again. Enter 'exit' to exit")
        admin()


def check_resources(water, coffee, milk):
    if resources["water"] - water <= 0:
        print("Please fill water first. Chose 'Fill'.")
        new_order()
    elif resources["coffee"] - coffee <= 0:
        print("Please fill coffee first. Chose 'Fill'.")
        new_order()
    elif resources["milk"] - milk <= 0:
        print("Please fill milk first. Chose 'Fill'.")
        new_order()


def end():
    print(f"Sorry the machine is empty. Chose another drink.")
    new_order()


def fill():
    done = False

    while not done:

        refill = input("What do you want to fill ?\n'w' for water\n'c' for coffee\n'm' for milk\n")
        quantity = int(input("Enter a quantity\n"))

        if refill == "w":
            resources["water"] += quantity
        if refill == "c":
            resources["coffee"] += quantity
        if refill == "m":
            resources["milk"] += quantity

        q = input("Are you done refilling?(y/n")
        if q == "y":
            done = True

    new_order()


def pay(cost):

    print(f' Your drink costs $ {cost}. Please enter coins')
    paid = 0
    while paid < cost:
        d = "'d' for dollars\n"
        q = "'q' for quarters\n"
        m = "'m' for dimes\n"
        n = "'n' for nickel\n"
        p = "'p' for penny\n"
        coin = input(f"{d}{q}{m}{n}{p}\n")

        if coin == "d":
            payments["dollars"] += 1
            paid += 1
            print(f"remaining : {cost - paid}.")

        if coin == "q":
            payments["quarters"] += 1
            paid += 0.25
            print(f"remaining : {cost - paid}.")

        if coin == "m":
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
        print(f"Your change is $ {change}.")

    payments["total"] += cost


def update_resources(water, coffee, milk):
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk


# Start machine here
new_order()
