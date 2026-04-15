# This file's purpose is to prompt the user for their item selection & quantity
import CalculateEligibility

header_line = "-=-=-=-=-=-=-=-=-"

# This method prompts the user to enter an item id and then a quantity. Both 
# are error checked and if succeed then the appropriate amount of items is
# sent back along with a True or False to signify a pass or fail. 
def select_item(container, user_info, mode):
    while(True):
        print("\nThis is the item selection screen. Choose an item id then the " +
        "quantity. To go back to the main menu, enter 'q'.")

        is_quitting = False
        item_id_input = input("\nDesired item id >>> ")

        if(item_id_input == "q"):
            is_quitting = True
            return False, -1, None

        matched_item_id = False
        item = ""

        matched_item_id, item = find_item_in_list(container, item_id_input)
        
        
        if matched_item_id:
            quantity_passed, quantity = get_quantity(item, user_info, mode)
                
            if quantity_passed:
                return True, quantity, item

        else:
            print(f"\nSorry, {item_id_input} does not match any of the item ids in the aisle. " \
                "Please try again!")
        
        if is_quitting:
            return False, -1, None
            
# This method takes in a container of items, which have
# sub-values of id, name, price, & weight, as well as an
# inputted item id; the items are iterated through and
# are checked if the inputted id and current item id
# match. 
def find_item_in_list(container, item_id_input):
    normalized_data = normalize_data(container)
    for item in normalized_data:
        if item[0] == None:
            return False, None
        if(item_id_input == item[0]['id']):
            return True, item
    return False, None


# This method takes in a container and normalizes the data; By
# 'normalizes' we mean wrap non tuple items into tuples with
# None as a placeholder for quantity.
def normalize_data(old_container):
    normalized_container = []
    for instance in old_container:
        if isinstance(instance, tuple) and len(instance) == 2 and isinstance(instance[1], (int, float)):
            # Already a (item, quantity) pair — unwrap and re-wrap to normalize the item
            item, quantity = instance
            if isinstance(item, tuple):
                # item is itself a wrapped tuple like ({...}, None) — unwrap it
                item = item[0]
            normalized_container.append((item, quantity))
        else:
            normalized_container.append((instance, None))
    return normalized_container

# This method takes in an item name to be used in printing for
# a quality of life feature for the user, and a user info
# structure. The user is prompted for a quantity of the item
# that was found. A check for a number between 0 & 9999
# (inclusive) sufficient funds and weight are conducted and
# if all pass then an according amount of funds and remaining
# weight are subtract from player data structure & an item and
# quantity are added to user's kart. 
def get_quantity(item, user_info, mode):
    while(True):
        try:
            inputted_quantity = input(f"Quantity of {item[0]['name']} (limit: 9999) >>> ")
            
            if(inputted_quantity == "q"):
                return True, -1

            inputted_quantity = int(inputted_quantity)

            if mode == "add":
                if validate_add(user_info, inputted_quantity, item):
                    return True, inputted_quantity
                else:
                    return False, -1
            else:
                if validate_remove(user_info, inputted_quantity, item):
                    return True, inputted_quantity
                else:
                    return False, -1

            

        except Exception as e:
            print("\nThat is not a number, please try again!")
            print(f"{e}; Please contact dev with a screenshot & how system was broken to " +
            "resolve this issue. <3")


# This method takes in the user_info object, inputted quantity, and 
# an item object. The purpose is to validate that the player has
# enough funds and remaining weight to add the number of requested
# items.  
def validate_add(user_info, inputted_quantity, item):
    if inputted_quantity == 0:
        return True

    if(0 <=(round(inputted_quantity))<= 9999):

        calculated_funds_passed = CalculateEligibility.calculate_valid_funds(user_info.get_wallet(), \
            inputted_quantity, item[0]['price'])

        if(calculated_funds_passed[0]):
            calculated_weight_passed = CalculateEligibility.calculate_valid_weight( \
                user_info.get_remaining_weight(), inputted_quantity, item[0]['weight'])

            if(calculated_weight_passed[0]):
                # Update user's funds, weight, & kart
                user_info.set_wallet_funds(user_info.get_wallet() - calculated_funds_passed[1])
                user_info.set_remaining_weight(user_info.get_remaining_weight() - calculated_weight_passed[1])
                user_info.add_item_to_kart(item, inputted_quantity)
                
                print(f"Added {inputted_quantity}x {item[0]['name']} to {user_info.get_kart_name()}")

                return True
                
            else:
                print(f"\nYou do not have enough weight in your kart for " \
                    f"{inputted_quantity}x {item[0]['name']}")
                return False
        else:
            print(f"\nYou do not have the funds for {inputted_quantity}x {item[0]['name']}...")
            return False
    
    else:
        print("\nThat input wasn't valid. Please enter an integer from 0-9999...")
        return False


# This method takes in the user_info object, inputted quantity, and an
# item object. The purpose is to check that the player has the selected
# item object in their kart. Then verify that the user has enough items
# in their kart to remove the requested quantity. Once the check is
# done, the item are removed from the player's kart then funds and 
# remaining weight are refunded. A True or False is returned depending
# if the method passed or failed to execute fully. 
def validate_remove(user_info, inputted_quantity, item):
    global header_line
    for index, player_item in enumerate(user_info.get_kart):

        if player_item[0][0]['id'] == item[0]['id']:

            if int(user_info.get_kart_subindex(index, 1)) >= inputted_quantity:

                if int(user_info.get_kart_subindex(index, 1)) == inputted_quantity:
                    user_info.remove_item_from_kart(player_item, inputted_quantity)
                    print(f"Removed {inputted_quantity}x {item[0]['name']} from kart\n" + \
                    f"{header_line}\nRemaining funds: {user_info.get_wallet()}\n" + \
                    f"Remaining weight: {user_info.get_remaining_weight()}")
                    return True

                user_info.remove_item_from_kart(item, inputted_quantity)
                return True
            
            else:
                print(f"\nCannot do that. {inputted_quantity} " +
                f"is larger than the amount of {item[0]['name']} " +
                f"in your {user_info.get_kart_name()}. (limit: " +
                f"{player_item[1]})")
                return False

    print(f"\nSorry, could not find {item[0]['name']} in " +
    f"your {user_info.get_kart_name()}")
    return False
