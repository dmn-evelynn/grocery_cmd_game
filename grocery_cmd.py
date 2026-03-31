import random
import json
# import math

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
        self.first_name = ""
        self.last_name = ""
        self.wallet = 0.00
        self.kart_preference = -1
        self.weight_limit = -1
        self.remaining_weight = self.weight_limit
        self.kart = []

    # Sets user's name
    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Adds funds to user's wallet
    def set_wallet_funds(self, wallet):
        self.wallet = wallet

    # Sets user's kart preference and then sets the maximum weight limit
    def set_kart_preference(self, kart_preference):
        self.kart_preference = kart_preference
        self.set_weight_limit()

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
        

# This method adds values to the Customer object. Calls generate_wallet &
# generate_kart_preference which handle the wallet and kart preference.
def create_user(user_info):

    # Prompts user to enter name and then calls the set_name constructor. Afterwards,
    # the generate_wallet & generate_kart_preference methods are called.
    print("....Welcome.....erm, you seem unfamiliar. Tell me a little about yourself!")
    user_info.set_name(input("First Name >>> "), input("Last Name >>> "))
    print(f"\nHi, {user_info.first_name} {user_info.last_name}! " +
          "Welcome on in....tell me a little bit more about yourself!")

    generate_wallet(user_info)

    generate_kart_preference(user_info)


# This method prompts the user to enter their starting wallet funds. Rounds input
# to two decimal places.
def generate_wallet(user_info):
    while (True):
        try:
            user_input = input("Starting Funds (X.XX) >>> ")
            if 0.01 > float(user_input) >= 1000000.00:
                print(
                    "\nAck!...That is not a valid input....Enter between 0 & 1,000,000.00")
            else:
                user_info.set_wallet_funds(round(float(user_input), 2))
                print(user_info.wallet)
                break
        except ValueError:
            print("\nAck!...That is not a valid input....Enter between 0 & 1,000,000.00")


# This method prompts the user to enter their kart preference. Afterwards, the max
# weight limit will be calculated and added to the user_info object.
def generate_kart_preference(user_info):
    print("""\nPerfect...now which size kart is your preference? Chose one of the numbers below:

              [1] Handbasket (Can hold  30lbs)
              [2] Small-kart (Can hold  75lbs)
              [3] Large-kart (Can hold 125lbs)

              """)
    while (True):
        user_input = input("Kart Preference [1,2,3] >>> ")
        # print(user_input)
        # print(type(user_input))
        if not (user_input == "1" or user_input == "2" or user_input == "3"):
            print("""\nAck!...That is not a valid input....Enter 1, 2, or 3:

              [1] Handbasket (Can hold  30lbs)
              [2] Small-kart (Can hold  75lbs)
              [3] Large-kart (Can hold 125lbs)

              """)
        else:
            user_info.set_kart_preference(user_input)
            break


# This method prints out the customer's stats along with a special first time message
def display_stats(user_info):
    breaker = '-~-' * 10
    first_visit = True

    if first_visit:
        print("\n...Let us take a look at your stats:")
        first_visit = False
    else:
        print("\nCustomer Stats:")

    print(breaker + "\n" +
          f"First Name       | {user_info.first_name}\n" +
          f"Last Name        | {user_info.last_name}\n" +
          f"Wallet           | {user_info.wallet:.2f}\n" +
          f"Weight Limit     | {user_info.weight_limit:.2f}\n" +
          f"Remaining Weight | {user_info.remaining_weight:.2f}\n" +
          breaker)


# This method shows the main menu screen to the user
def player_choose_from_menu(user_info):
    first_visit = True

    while (True):
        random_dialog_choice = random.randint(1, 3)
        #print(random_dialog_choice)
        if (first_visit):
            print(f"\nAlright, {user_info.first_name}, let's get the ball rolling...." +
                  "Choose from one of the following options:\n")
            first_visit = False
        elif (random_dialog_choice < 2):
            # <------ Finish this
            print("\nPlease select from the following options:")
        else:
            print("\nPick one of the options below to continue:")

        print("""
        [1] Aisle selection
        [2] View your stats
        [3] Head to checkout
        [4] Quit\n""")
        user_input = input("Your selection >>> ")
        if not (user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4"):
            print("""\nAck!...That is not a valid input....Enter 1, 2, 3, or 4:

                    [1] Aisle selection
                    [2] View your stats
                    [3] Head to checkout
                    [4] Quit\n""")

            user_input = input("Your selection >>> ")
        elif user_input == "1":
            enter_aisles(user_info)
            del user_input
        elif user_input == "2":
            display_stats(user_info)
            del user_input
        elif user_input == "3":
            checkout(user_info)
            del user_input
        elif user_input == "4":
            print("It is sad to see you go....")
            break


# This method allows the user to chose an aisle, learn more about each aisle, or
# return to the main menu.
def enter_aisles(user_info):
    create_file = True
    if (create_file):
        create_aisle_file()
        create_file = False
        
    
        
    print("""\nWhich aisle will you go to? Choose from the following:

        [1] Meat
        [2] Dairy
        [3] Fauna
        [4] Baking Needs
        [5] Cleaning Supplies
        [6] Checkout
        [7] Back to Main Menu\n""")
    user_input = input("Your selection >>> ")

    while (True):
        break_out_while = False
        if not (user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5" or user_input == "6" or user_input == "7"):
            print("""\nAck!...That is not a valid input....Enter 1, 2, 3, 4, 5, 6, or 7:

        [1] Meat
        [2] Dairy
        [3] Fauna
        [4] Baking Needs
        [5] Cleaning Supplies
        [6] Checkout
        [7] Back to Main Menu\n""")
            user_input = input("Your selection >>> ")
            
        else:
            
            match user_input:
                case "1" | "2" | "3" | "4" | "5":
                    #run thru methods
                    aisles = read_aisle_file()
                    item_view_menu(aisles, user_input,user_info)
                    #return to previous menu
                    break
                case "6":
                    checkout(user_info)
                    break_out_while = True
                    break
                case "7":
                    break_out_while = True
                    break
                
            if(break_out_while):
                break
            
        
    # Aisle Layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Aisle 1 -     Meat (ground beef, chicken, bacon, turkey)
    # Aisle 2 -    Dairy (milk, eggs, cheese, butter)
    # Aisle 3 -    Fauna (lettuce, apples, oranges, bananas)
    # Aisle 4 -   Baking (baking soda, salt, oil, bowls)
    # Aisle 5 - Cleaning (paper towel, bleach, brush, air refreshener)
    # Checkout
    # Quit

#"id": "", "name": "", "price": 
def create_aisle_file():
    #print("Creating File")
    aisles_data = {
        "aisles":[
            {
               "aisle_number": "1",
               "aisle_name": "Meat",
               "items":[
                   {"id": "101", "name": "ground beef", "price": 6.75, "weight": 3.00},
                   {"id": "102", "name": "chicken", "price": 5.50, "weight": 2.75},
                   {"id": "103", "name": "bacon", "price": 2.35, "weight": 1.05},
                   {"id": "104", "name": "turkey", "price": 8.00, "weight": 7.50}
                   ]
                },
            {
                "aisle_number": "2",
                "aisle_name": "Dairy",
                "items":[
                    {"id": "201", "name": "milk", "price": 2.15, "weight": 2.85},
                    {"id": "202", "name": "egg (x6)", "price": 2.65, "weight": 0.95},
                    {"id": "203", "name": "egg (x12)", "price": 4.15, "weight": 2.00},
                    {"id": "204", "name": "cheese", "price": 1.05, "weight": 1.00},
                    {"id": "205", "name": "butter", "price": 0.85, "weight": 0.50},
                    ]
                },
            {
                "aisle_number": "3",
                "aisle_name": "Fauna",
                "items":[
                    {"id": "301", "name": "apple", "price": 2.20, "weight": 1.15},
                    {"id": "302", "name": "banana", "price": 0.95, "weight": 1.10},
                    {"id": "303", "name": "orange", "price": 1.75, "weight": 1.15},
                    {"id": "304", "name": "lettuce", "price": 1.50, "weight": 1.45}
                    ]
                },
            {
                "aisle_number": "4",
                "aisle_name": "Baking",
                "items":[
                    {"id": "401", "name": "baking soda", "price": 3.15, "weight": 0.45},
                    {"id": "402", "name": "salt", "price": 1.05, "weight": 0.65},
                    {"id": "403", "name": "cooking oil", "price": .85, "weight": 1.05},
                    {"id": "404", "name": "mixing bowl set", "price": 5.75, "weight": 3.75}
                    ]
                },
            {
                "aisle_number": "5",
                "aisle_name": "Cleaning Products",
                "items":[
                    {"id": "501", "name": "paper towel", "price": 3.60, "weight": .85},
                    {"id": "502", "name": "bleach", "price": 4.00, "weight": 1.65},
                    {"id": "503", "name": "brush", "price": 2.50, "weight": 1.25},
                    {"id": "504", "name": "air refreshener", "price": 3.15, "weight": 1.30}
                    ]
                }
            ]
        }
    
    with open("aisles.json", "w") as json_file:
        json.dump(aisles_data, json_file, indent=4)

#
# Read data in from fileeeee
#


def read_aisle_file():
    #print("Reading File")
    try:
        with open('aisles.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'data.json' not found. Please ensure the file exists.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'data.json'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def checkout(user_info):
    if user_info.kart == []:
        print(
            f"\n...Oops, apologies {user_info.first_name}...You need to add some items to your kart!...")
    else:
        print("Checking out...")


def item_view_menu(aisles, user_input,user_info):
    for aisle in aisles['aisles']:
        if(user_input == aisle['aisle_number']):
            #print(f"Match\t{user_input}\t{aisle['aisle_name']}")
            
            items = []
            highest_line_length = 0
            highest_item_length = 0
            
            for item in aisle['items']:
                if(highest_item_length < len(item['name'])):
                    highest_item_length = len(item['name'])
            
            for item in aisle['items']:
                spacing = ' ' * (highest_item_length - len(item['name']))
                    
                line = f"| item id | {item['id']} ||\t|| item name | {item['name']}{spacing} ||\t|| item price | {item['price']:.2f} ||\t|| item weight | {item['weight']:.2f} |"
                
                items.append(line)
                
                if(highest_line_length < len(line)):
                    highest_line_length = len(line)
            #=========
            #Fix divder length and make two methods to get item name spacing and divider length
            #=========
            divider = '=' * (highest_line_length + 1)
            print(f"+{divider}+")
            for item in items:
                print(item)
            
            print(f"+{divider}+")


user_info = Customer()
create_user(user_info)
display_stats(user_info)
player_choose_from_menu(user_info)
# enter_aisles(user_info)
# checkout(user_info)

# print(f"Kart pref: {user_info.kart_preference}")
# print(f"Weight Limit: {user_info.weight_limit}")

# print(
#     f"kart type: {type(user_info.kart_preference)} & kart: {user_info.kart_preference}")
# print(f"wallet: {user_info.wallet}")
print(".....Thank you for playing! :D")
