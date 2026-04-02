# This file's purpose is to prompt the user for their item selection & quantity
import CalculateEligibility

def select_item(aisle, aisle_number_input, user_info):
    print("This is the item selection screen. Choose an item id then the quantity. To go back to the main menu, enter 'q'.")
    while(True):
        is_quiting = False
        item_id_input = input("\nDesired item id >>> ")

        if(item_id_input == "q"):
            break

        matched_item_id = False
        item = ""

        for item in aisle['items']:
            if(item_id_input == item['id']):
                matched_item_id = True
                item_name = item['name']
                break
        
        if matched_item_id:
            while(True):
                try:
                    inputed_quantity = input(f"Quantity of {item_name} (limit: 9999) >>> ")
                    if(inputed_quantity == "q"):
                        is_quiting = True
                        break
                    else:
                        inputed_quantity = int(inputed_quantity)

                    if(0 <=(round(inputed_quantity))<= 9999):
                        # user's wallet funds, the quantity,
                        # & the selected item's price
                        # print(f"{user_info.wallet}\n{inputed_quantity}\n{int(item['price'])}")

                        calculated_funds = CalculateEligibility.calculate_valid_funds(user_info.wallet, \
                            inputed_quantity, item['price'])

                        if(calculated_funds[0]):
                            calculated_weight = CalculateEligibility.calculate_valid_weight( \
                                user_info.remaining_weight, inputed_quantity, item['weight'])

                            if(calculated_weight[0]):
                                print(f"\n\n{user_info.wallet}\n{user_info.remaining_weight}")

                                user_info.set_wallet_funds((user_info.wallet - calculated_funds[1]))

                                difference = (user_info.remaining_weight - calculated_weight[1])
                                user_info.set_remaining_weight(difference)

                                print(f"\n\n{user_info.wallet}\n{user_info.remaining_weight}")
                                break
                            else:
                                print(f"\nYou do not have enough weight in your kart for " \
                                    "{inputed_quantity}x {item['name']}")
                        else:
                            print(f"\nYou do not have the funds for {inputed_quantity}x {item['name']}...")
                    #=====
                    #Continue Here :3
                    #=====
                    else:
                        print("\nThat input wasn't valid. Please enter an integer from 0-9999...")
                except Exception as e:
                    print("\nThat is not a number, please try again!")
                    print(f"{e}; Please contact dev with a screenshot & how systme was broken to resolve this issue. <3")
        else:
            print(f"\nSorry, {item_id_input} does not match any of the item ids in the aisle. " \
                "Please try again!")
        
        if(is_quiting):
            break
            