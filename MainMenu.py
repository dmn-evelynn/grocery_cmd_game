# This file's purpose is to act as the main menu screen; user can go to aisles, view their stats, or head to checkout

import random
import AisleMenu, DisplayStats, Checkout, CalculateEligibility

# This method shows the main menu screen to the user
def player_choose_from_menu(user_info):
    first_visit = True
    menu = """\t[1] Aisle selection
        [2] View your stats
        [3] Remove items from kart
        [4] Head to checkout
        [5] Quit\n"""

    while (True):
        random_dialog_choice = random.randint(1, 3)
        #print(random_dialog_choice)
        if (first_visit):
            print(f"\nAlright, {user_info.name}, let's get the ball rolling...." +
                  "Choose from one of the following options by inputting an integer:\n")
            first_visit = False
        elif (random_dialog_choice < 2):
            print("\nPlease select from the following options:")
        else:
            print("\nPick one of the options below to continue:")

        print(menu)
        user_input = input("Your selection >>> ")

        while(True):
            if not (user_input == "1" or user_input == "2" or \
                user_input == "3" or user_input == "4" or \
                    user_input == "5" or user_input == "q"):
                print("\nAck!...That is not a valid input....Enter 1, 2, 3, 4 or 5:")
                print(menu)
                user_input = input("Your selection >>> ")
            else:
                break
        if user_input == "1":
            AisleMenu.enter_aisles(user_info)
            del user_input
        elif user_input == "2":
            DisplayStats.display_stats(user_info)
            del user_input
        elif user_input == "3":
            CalculateEligibility.remove_item_from_kart(user_info)
            del user_input
        elif user_input == "4":
            Checkout.checkout(user_info)
            del user_input
        elif user_input == "5" or user_input == "q":
            print("It is sad to see you go....")
            break
