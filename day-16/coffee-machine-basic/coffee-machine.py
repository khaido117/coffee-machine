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

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
           if order_ingredients[item] >= resources[item]:
                 print(f"Sorry, there is not enought {item}")
                 return False
    return True 

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False if money if insufficient."""
    if money_received < drink_cost:
            print("Sorry, that's not enough money. Money refunded. Please try again.")
            return False
    else:
        change = round(money_received - drink_cost,2)
        global profit
        profit += drink_cost
        print(f"Here is {change} in change.")
        return True
        
            
def process_coins():
      """Returns the total caculated from coins inserted."""
      total = int(input("How many quarters?: ")) * 0.25
      total += int(input("How many dimes?: ")) * 0.1
      total += int(input("How many nickles?: ")) * 0.05
      total += int(input("How many pennies?: ")) * 0.01
      return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
            resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ")


#Ask what would you order?
profit = 0
is_on = True 
while is_on: 
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
            print("The machine coffee has been turned off. ")
        elif choice == "report":
            for ingre in resources:
                    print (f"{ingre}: {resources[ingre]}ml")
            print(f"Money: {profit}")
        elif choice in ["espresso", "latte", "cappuccino"]:
              drink = MENU[choice]
              if is_resource_sufficient(drink["ingredients"]):
                paid = process_coins()
                if is_transaction_successful(paid, MENU[choice]["cost"]):
                      make_coffee(choice, drink["ingredients"])
                      
        else:
              print("Invalid choice. Please enter valid drinks of 'off'. ")
