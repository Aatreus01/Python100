from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


while(True):
    
    user_input = input(f"What would you like? ({menu.get_items()})")
    
    match user_input:
        case "off":
            exit()
        case "report":
            coffee_machine.report()
        case _:
            order = menu.find_drink(user_input)
            can_make = coffee_machine.is_resource_sufficient(order)
            if can_make:
                transaction_completed = money_machine.make_payment(order.cost)
                if transaction_completed:
                    coffee_machine.make_coffee(order)

