
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

machine_on = True

money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def resource_report(rwater, rmilk, rcoffee, rmoney):
    print(f"Water: {rwater} ml")
    print(f"Milk: {rmilk} ml")
    print(f"Coffee: {rcoffee} g")
    print(f"Money: $ {rmoney}")


def check_resources(drink, rwater, rmilk, rcoffee):
    if MENU[drink]["ingredients"]["water"] > rwater:
        print("Sorry, there is not enough water")
    elif MENU[drink]["ingredients"]["coffee"] > rcoffee:
        print("Sorry there is not enough coffee")
    elif drink != "espresso" and MENU[drink]["ingredients"]["milk"] > rmilk:
        print("Sorry there is not enough milk")
    else:
        print(f"The drink costs ${MENU[drink]['cost']}0. Please insert coins.")
        return True


def calculate_money(drink):
    quarters = int(input("How Many Quarters: "))
    dimes = int(input("How Many Dimes: "))
    nickles = int(input("How Many Nickles: "))
    pennies = int(input("How Many Pennies: "))
    return quarters * .25 + dimes * .1 + nickles * .05 + pennies * .01


#TODO 3: make change two decimal places
def check_money(drink, cmoney):
    print(f"The drink costs $ {MENU[drink]['cost']}0, and you paid $ {cmoney:.2f}.")
    if MENU[drink]["cost"] == cmoney:
        return True
    elif MENU[drink]["cost"] > cmoney:
        print(f"Sorry that is not enough money. Money refunded.")
        return False
    elif MENU[drink]["cost"] < cmoney:
        change = cmoney - MENU[drink]["cost"]
        print(f"You overpaid. You get $ {change:.2f} change.")
        return True

def update_resources(drink, rwater, rmilk, rcoffee, rmoney):
    new_water = rwater - MENU[drink]["ingredients"]["water"]
    new_coffee = rcoffee - MENU[drink]["ingredients"]["coffee"]
    new_money = rmoney + MENU[drink]["cost"]
    if drink != "espresso":
        new_milk = rmilk - MENU[drink]["ingredients"]["milk"]
    else:
        new_milk = rmilk
    return new_water, new_milk, new_coffee, new_money


#Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#Turn off the Coffee Machine by entering “off” to the prompt
#Print report.

while machine_on == True:
    selection = (input("What would you like? (espresso/latte/cappuccino): ").lower())
    if selection == "off":
        machine_on = False
    elif selection == "report":
        resource_report(water, milk, coffee, money)
    elif selection == "espresso" or "latte" or "cappuccino":
        drink_supplies = check_resources(selection, water, milk, coffee)
        if drink_supplies == True:
            money_insert = calculate_money(selection)
            money_supplies = check_money(selection, money_insert)
            if money_supplies == True:
                water, milk, coffee, money = update_resources(selection, water, milk, coffee, money)
                print(f"Here is your {selection}. Enjoy!")

print("Coffee Machine is Off")


