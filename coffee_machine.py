
from coffee_menu import MENU,resources
is_on = True
# need to keep a trackk of the money
profit = 0
# make a funcion to compare the rescores from the drink and how many are left
def is_recorces_sufficient(order_ingredients):
     """Returns true if the order can be made and flase if the ingredients are not sufficent"""
     # TO keep a track of the ingredients
     is_enough = True
     for items in order_ingredients:
          if order_ingredients[items] >= resources[items]:
               print(f"Sorry there is not enough {items}.")
               is_enough = False
     return True

# FUnctions to process coins
def process_coins():
     """It returns the total calculated from the coins inserrted."""
     print("Please insert coins")
     total = int(input("How many quaters?: "))*0.25
     total += int(input("How many dimes?: "))*0.10
     total += int(input("How many nickle?: "))*0.05
     total += int(input("How many pennies?: "))*0.01
     return total

def trancation_successful(money_recived, drink_cost):
     """Returns true is the amount is accepted or returns false if the money is not sufficent."""
     if money_recived >= drink_cost:
         change = round(money_recived - drink_cost,2)
         print(f"Here is ${change} in change.")
         # profit is in golabl scope andwe need to use in the local scope so we use the vvariable global
         global profit
         profit += drink_cost
         return True
     else:
          print("Sorry , That's not enough . Money si refunded")
          return False
          
def make_coffee(drink_name, order_ingredients):
     """Deducct the required ingredients from the rescorces. """
     for items in order_ingredients:
          resources[items] -= order_ingredients[items]
     print(f"Here is your {drink_name} ☕")      

# ask for the user prefernce. This questions needs to be asked again so we use a loop
while is_on:
    user_input = input("What would you like ? (espresso/latte/cappuccino):  ")
    # when we want to stop the coffee machine we use a word off
    if user_input == "off":
         is_on =False
    elif user_input == "report":
          print(f"Water: {resources['water']}ml") 
          print(f"Milk: {resources['milk']}ml")
          print(f"Coffee: {resources['coffee']}g")
          print(f"Money: ${profit}")  
    else:
         drink = MENU[user_input]
         
         # if the ingridents are sufficent then we can move to process the coins
         if is_recorces_sufficient(drink["ingredients"]):
              payment = process_coins()
              if trancation_successful(payment,drink["cost"]):
                   make_coffee(user_input,drink["ingredients"])