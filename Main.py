# This file's purpose is to be Main file

import CreateUser, DisplayStats, MainMenu, AddRemoveItems

# This program attempts to give the user a grocery shopping experience
# via text prompts and text responses.

# [1] Method that gets called to start up game and welcome player.
# [2] Method that repeats until user types something.
# [3] Method that handles sub methods creating the shopping kart and creating
# user info/wallet
# [4] Method that handles asking customer what aisle they want to go to
# [5] Method that handles giving a description from user entry
# [6] Method that handles choosing an item
# [7] Method that handles viewnig customer's kart
# [8] Method that handles viewing customer's info/wallet
# [9] Method that handles removing an item
# [10] Method that handles [THREE DIFFERENT SHOPPING KARTS WITH DIFFERENT weight_limit
# CAPACITIES]
# [11] Method that handles checking out
# [12] Method that handles employee having a light convo with you
# [13] Method that handles some of the user's stats



# Class created to house user info
class Customer:
    # Data points initialized upon object creation
    def __init__(self):
        self.name = ""
        self.wallet = 0.00
        self.kart_preference = -1
        self.weight_limit = -1
        self.remaining_weight = self.weight_limit
        self.kart = []

    # Sets user's name
    def set_name(self, name):
        self.name = name

    # Adds funds to user's wallet
    def set_wallet_funds(self, wallet):
        self.wallet = wallet

    # Sets user's kart preference and then sets the maximum weight limit
    def set_kart_preference(self, kart_preference):
        self.kart_preference = kart_preference
        self.set_weight_limit()

    # Sets the weight limits for each kart preference
    def set_weight_limit(self):
        basket = 30
        small_kart = 75
        large_kart = 125

        if self.kart_preference == "1":
            self.weight_limit = basket
        elif self.kart_preference == "2":
            self.weight_limit = small_kart
        elif self.kart_preference == "3":
            self.weight_limit = large_kart

        # Updates remaining weight value
        self.remaining_weight = self.weight_limit
    
    # Updates remaining weight variable
    def set_remaining_weight(self, remaining_weight):
        self.remaining_weight = remaining_weight

    # Adds items to the player's kart
    def add_item_to_kart(self, item, quantity):
        AddRemoveItems.add_item(self, item, quantity)
        print(f"Added {quantity}x {item['name']} to kart")
        

    # Displays the player's current kart
    def display_kart(self, id_value: str = None):
        header = f"\nDisplaying {self.name}'s {self.get_kart_name()}:\n===========\n\t==\n=========================="
        if id_value == "id's":
            print(header)

            for item, quantity in self.kart:
                print(f"id: {item['id']} | {quantity:04d}x | {item['name']}")

        else:
            print(header)
            # print(self.kart)
            for item, quantity in self.kart:
                print(f"{quantity:04d}x | {item['name']}")


    # Returns the name for kart preference
    def get_kart_name(self):
        if self.kart_preference == "1":
            return "basket"
        elif self.kart_preference == "2":
            return "small kart"
        elif self.kart_preference == "3":
            return "large kart"
    
    # Removes selected item & quantity from player's kart
    def remove_item_from_kart(self, item, quantity):
        AddRemoveItems.remove_item(self, item, quantity)
        

user_info = Customer()
# player_choose_from_menu(user_info)
CreateUser.create_user(user_info) # <- Own file
DisplayStats.display_stats(user_info) # <- Own file
MainMenu.player_choose_from_menu(user_info) # <- Own file
# enter_aisles(user_info)
# checkout(user_info)

# print(f"Kart pref: {user_info.kart_preference}")
# print(f"Weight Limit: {user_info.weight_limit}")

# print(
#     f"kart type: {type(user_info.kart_preference)} & kart: {user_info.kart_preference}")
# print(f"wallet: {user_info.wallet}")
print(".....Thank you for playing! :D")
