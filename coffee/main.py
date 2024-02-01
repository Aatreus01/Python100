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
    "money": 0,
}

def take_order():
    order = input("What would you like? (espresso/latte/cappuccino)")
    match order:
        case "espresso":
            return order
        case "latte":
            return order
        case "cappuccino":
            return order
        case "off":
            exit()          
        case "report":
            print(f'Water: {resources["water"]} ml',
                f'\nMilk: {resources["milk"]} ml',
                f'\nCoffee: {resources["coffee"]} g',
                f'\nMoney: {resources["money"]} $')
            return order
        case _:
            print("Please input a valid argument")
            exit()

def check_resources(order):
    if(MENU[order]["ingredients"]["water"] > resources["water"]):
        print("Sorry, there is not enough water")
        return True
    elif(order != "espresso" and MENU[order]["ingredients"]["milk"] > resources["milk"]):
        print("Sorry there is not enough milk")
        return True
    elif(MENU[order]["ingredients"]["coffee"] > resources["coffee"]):
        print("Sorry there is not enough coffee")
        return True

def coin_insert():
    quarters_amount = 0.25*float(input("How many quarters?"))
    dimes_amount = 0.10*float(input("How many dimes?"))
    nickles_amount = 0.05*float(input("How many nickles?"))
    pennies_amount = 0.01*float(input("How many pennies?"))
    total_money = quarters_amount+dimes_amount+nickles_amount+pennies_amount
    return total_money

def check_money(money, order):
    cost = MENU[order]["cost"]
    if(money > cost):
        change = round(money - cost, 2)
        print(f"Here is ${change} dollars in change")
        resources["money"] += cost
    elif(money == cost):
        resources["money"] += cost
    else:
        print(f"Sorry that's not enough money(cost: {cost}, you paid: {money}). Money refunded")
        return True

def coffee_make(order):
    water_cost, coffee_cost = MENU[order]["ingredients"]["water"], MENU[order]["ingredients"]["coffee"]
    milk_cost = 0
    if (order != "espresso"):
        milk_cost = MENU[order]["ingredients"]["milk"]
    resources["water"] -= water_cost
    resources["milk"] -= milk_cost
    resources["coffee"] -= coffee_cost
    print(f"Here is your {order}. Enjoy!")

while(True):
    order = take_order()
    if(order =="report"): continue
    if(check_resources(order)): continue
    user_money = coin_insert()
    if(check_money(user_money, order)): continue
    coffee_make(order)