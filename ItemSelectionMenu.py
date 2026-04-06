# This file's purpose is to prompt the user for their item selection & quantity
import CalculateEligibility

# This method prompts the user to enter an item id and then a quantity. Both 
# are error checked and if succeed then the appropriate amount of items is
# sent back along with a True or False to signify a pass or fail. 
def select_item(container, user_info):
    print("This is the item selection screen. Choose an item id then the " +
    "quantity. To go back to the main menu, enter 'q'.")
    while(True):
        is_quitting = False
        item_id_input = input("\nDesired item id >>> ")

        if(item_id_input == "q"):
            return False, -1

        matched_item_id = False
        item = ""

        matched_item_id, item_name = find_item_in_list(container, item_id_input)
        
        
        if matched_item_id:
            while(True):
                quantity_passed, quantity = get_quantity(item_name, user_info)
                if quantity_passed:
                    return True, quantity
        else:
            print(f"\nSorry, {item_id_input} does not match any of the item ids in the aisle. " \
                "Please try again!")
        
        if(is_quitting):
            return False, -1
            
# This method takes in a container of items, which have
# sub-values of id, name, price, & weight, as well as an
# inputted item id; the items are iterated through and
# are checked if the inputted id and current item id
# match. 
def find_item_in_list(container, item_id_input):
    for item in container:
        if(item_id_input == item['id']):
            return True, item['name']

# This method takes in an item name to be used in printing for
# a quality of life feature for the user, and a user info
# structure. The user is prompted for a quantity of the item
# that was found. A check for a number between 0 & 9999
# (inclusive) sufficient funds and weight are conducted and
# if all pass then an according amount of funds and remaining
# weight are subtract from player data structure & an item and
# quantity are added to user's kart. 
def get_quantity(item_name, user_info):
    try:
        inputted_quantity = input(f"Quantity of {item_name} (limit: 9999) >>> ")
        
        if(inputted_quantity == "q"):
            is_quitting = True
            return True, -1
        else:
            inputted_quantity = int(inputted_quantity)

        if(0 <=(round(inputted_quantity))<= 9999):
            # user's wallet funds, the quantity, & the selected item's price
            # print(f"{user_info.wallet}\n{inputted_quantity}\n{int(item['price'])}")

            calculated_funds = CalculateEligibility.calculate_valid_funds(user_info.wallet, \
                inputted_quantity, item['price'])

            if(calculated_funds[0]):
                calculated_weight = CalculateEligibility.calculate_valid_weight( \
                    user_info.remaining_weight, inputted_quantity, item['weight'])

                if(calculated_weight[0]):
                    # print(f"\n\n{user_info.wallet}\n{user_info.remaining_weight}")

                    user_info.set_wallet_funds((user_info.wallet - calculated_funds[1]))

                    difference = (user_info.remaining_weight - calculated_weight[1])
                    user_info.set_remaining_weight(difference)

                    # print(f"\n\n{user_info.wallet}\n{user_info.remaining_weight}")
                    user_info.add_item_to_kart(item, inputted_quantity)
                    return True, inputted_quantity
                else:
                    print(f"\nYou do not have enough weight in your kart for " \
                        "{inputted_quantity}x {item['name']}")
                    return False, -1
            else:
                print(f"\nYou do not have the funds for {inputted_quantity}x {item['name']}...")
                return False, -1
        
        else:
            print("\nThat input wasn't valid. Please enter an integer from 0-9999...")
            return False, -1
    except Exception as e:
        print("\nThat is not a number, please try again!")
        print(f"{e}; Please contact dev with a screenshot & how system was broken to " +
        "resolve this issue. <3")
        return False, -1