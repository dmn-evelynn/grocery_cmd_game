# This file handles calculating if the user has enough funds and an appropriate
# amount of weight for their selected item(s).
import AddRemoveItems

# This method takes in the user's wallet funds, the quantity,
# & the selected item's price. The user's wallet funds is compared to the quantity
# of selected items time the price; this comparison is sent back as a True or False
# to be used in deciding to move on or send user back to item selction screen.
def calculate_valid_funds(funds, quantity, price):
    if funds > round((quantity * price), 2):
        # print(f"{funds} vs {round((quantity * price), 2)}")

        return True, round((quantity * price), 2)
    else:
        # print(f"{funds} vs {round((quantity * price), 2)}")
        return False, round((quantity * price), 2)


# This method takes in the user's remaining weight limit, the quantity, & the
# selected item's weight. The user's remaining weight limit is compared to
# the item's weight times the quantity; The comparison then sends back a True
# or False depending on the outcome.
def calculate_valid_weight(remaining_weight, quantity, item_weight):
    if remaining_weight > round((quantity * item_weight), 2):
        # print(f"{remaining_weight} vs {round((quantity * item_weight), 2)}")

        return True, round((quantity * item_weight), 2)
    else:
        # print(f"{remaining_weight} vs {round((quantity * item_weight), 2)}")
        return False, round((quantity * item_weight), 2)


# This method takes in the quantity of items in the player's kart and the
# inputted quantity; a comparison is made to verify that the difference
# won't be a negative number
def determine_quantity_subtraction_eligibility(kart_quantity, inputted_quantity):
    if((int(kart_quantity) - int(inputted_quantity) > 0)):
        return True
    else:
        return False


# This method takes in user_info and checks if the player's kart has any items
# in it; if true then the player is prompted to input the item's id # and then
# quantity. Both values are error checked with same logic as adding an item to
# kart; if false then the user is informed to add items to kart first.
def remove_item_from_kart(user_info):
    if not user_info.kart:
        print(f"\nCannot do that... Please add some items to your {user_info.get_kart_name()} and then try again!")
    else:
        user_info.display_kart("id's")
        AddRemoveItems.get_item_plus_quantity()