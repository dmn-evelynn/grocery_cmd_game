# This file's purpose is to act as the main menu screen;
# user can go to aisles, view their stats, or head to checkout
from random import randint
import AisleMenu, DisplayStats, Checkout, CalculateEligibility

options = ["Aisle Selection", "View Yours Stats", \
    "Remove Items From Kart", "Head To Checkout"]

first_visit = True
print_error = False

user_input = ""

# This method takes in a user_info object; it globalizes
# options, print_error, & user_input; Infinite while loop
# that prints out either a header or error message along 
# with selectable options; User is prompted for integer
# value; Inputted value is error checked and then 
# checked for dynamic and predetermined options. 
def player_choose_from_menu(user_info):
    global options, print_error, user_input

    while True:
        print(make_header(options, user_info))
        print(print_options(options))

        try:
            user_input = int(input("\nYour selection >>> "))
        except ValueError:
            print_error = True
            continue

        if user_input == len(options) + 1:
            print("\nIt is sad to see you go....")
            break

        if user_input == len(options):
            Checkout.checkout(user_info)
            continue

        if user_input == len(options) - 1:
            CalculateEligibility.remove_item_from_kart(user_info)
            continue

        if user_input == len(options) - 2:
            DisplayStats.display_stats(user_info)
            continue

        if user_input == len(options) - 3:
            AisleMenu.enter_aisles(user_info)
            continue

        print_error = True


# This method takes in an options list and a user_info object;
# it globalizes first_visit & print_error; returns an error 
# message if print_error is set to True; a random number either
# 1 or 2 is generated and is used to display a random dialogue
# option unless it is the first time; if first time then a 
# header that says to enter an integer is return. 
def make_header(options, user_info):
    global first_visit, print_error
    random_dialog_choice = randint(1, 2)

    if print_error:
        print_error = False
        return f"\nAck!...That is not a valid input....Enter 1 - {len(options) + 1}"

    if first_visit:
        first_visit = False
        return f"\nAlright, {user_info.name}, let's get the ball rolling...." \
                "Choose from one of the following options by inputting an integer:"
    elif (random_dialog_choice == 2):
        return "\nPlease select from the following options:"
    else:
        return "\nPick one of the options below to continue:"


# This method takes in an options list; it iterates through the list
# and creates a menu from it; adds a Quit option as well; returns string. 
def print_options(options):
    menu = ""

    for i, option in enumerate(options, start=1):
        menu += f"\t[{i}] {option}\n"
    menu += f"\t[{len(options) + 1}] Quit"

    return menu