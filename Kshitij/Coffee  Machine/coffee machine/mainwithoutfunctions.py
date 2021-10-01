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

# TODO 1.Reuccuring prompt
# TODO 2. Print Report
# TODO 3. Check Resources
# TODO 4. Process Coins
# TODO 5.Check Transaction
# TODO 6.makecoffee
money = 0
while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if(user_input == "OFF" or user_input == "off"):
        break
    if(user_input == "report"):
        for key, value in resources.items():
            print(f'{key}:{value}')
        print(f'Money:${money}')
    if(user_input == "espresso"):
        if(MENU["espresso"]["ingredients"]["water"] > resources["water"]):
            print("“Sorry there is not enough water.")
        if (MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]):
            print("“Sorry there is not enough coffee.")
        else:
            # resources["coffee"] = resources["coffee"]-MENU["espresso"]["ingredients"]["coffee"]
            # resources["water"]=resources["water"]-MENU["espresso"]["ingredients"]["water"]
            #! we have checked resources and we will update them if coins are right
            print("Please insert Coins")
            quaters = int(input("How many Quaters? : "))
            dimes = int(input("How many Dimes? : "))
            nickels = int(input("How many Nickels? : "))
            pennies = int(input("How many Pennies? : "))
            user_coin = quaters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
            if(user_coin < MENU["espresso"]["cost"]):
                print("“Sorry that's not enough money. Money refunded")
                user_coin = 0
            else:
                money = money+MENU["espresso"]["cost"]
                resources["coffee"] = resources["coffee"] - \
                    MENU["espresso"]["ingredients"]["coffee"]
                resources["water"] = resources["water"] - \
                    MENU["espresso"]["ingredients"]["water"]
                money_return = user_coin-MENU["espresso"]["cost"]
                print(f'Here is ${money_return} in change,')
                print("Here is your espresso ☕. Enjoy!")
    

    if(user_input == "latte"):
        if(MENU["latte"]["ingredients"]["water"] > resources["water"]):
            print("“Sorry there is not enough water.")
        if (MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]):
            print("“Sorry there is not enough coffee.")
        if (MENU["latte"]["ingredients"]["milk"] > resources["milk"]):
            print("“Sorry there is not enough milk.")
        else:
           
           
            #! we have checked resources and we will update them if coins are right
            print("Please insert Coins")
            quaters = int(input("How many Quaters? : "))
            dimes = int(input("How many Dimes? : "))
            nickels = int(input("How many Nickels? : "))
            pennies = int(input("How many Pennies? : "))
            user_coin = quaters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
            if(user_coin < MENU["latte"]["cost"]):
                print("“Sorry that's not enough money. Money refunded")
                user_coin = 0
            else:
                money = money+MENU["latte"]["cost"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                money_return = user_coin-MENU["latte"]["cost"]
                print(f'Here is ${money_return} in change,')
                print("Here is your latte ☕. Enjoy!")


    if(user_input == "cappuccino"):
        if(MENU["cappuccino"]["ingredients"]["water"] > resources["water"]):
            print("“Sorry there is not enough water.")
        if (MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]):
            print("“Sorry there is not enough coffee.")
        if (MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]):
            print("“Sorry there is not enough milk.")
        else:
           
           
            #! we have checked resources and we will update them if coins are right
            print("Please insert Coins")
            quaters = int(input("How many Quaters? : "))
            dimes = int(input("How many Dimes? : "))
            nickels = int(input("How many Nickels? : "))
            pennies = int(input("How many Pennies? : "))
            user_coin = quaters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
            if(user_coin < MENU["cappuccino"]["cost"]):
                print("“Sorry that's not enough money. Money refunded")
                user_coin = 0
            else:
                money = money+MENU["cappuccino"]["cost"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                money_return = user_coin-MENU["cappuccino"]["cost"]
                print(f'Here is ${money_return} in change,')
                print("Here is your cappuccino ☕. Enjoy!")


     

