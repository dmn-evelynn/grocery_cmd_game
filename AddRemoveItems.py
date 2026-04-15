# This file manages methods for adding and removing items from the player's kart.
import CalculateEligibility, ItemSelectionMenu

# This method checks the player's kart for alike items and then adds new quantity
# to existing quantity; if alike items are not found then a new entry it made.
def add_item(user_options, item, quantity):
    # Method that searches kart list for same item entry; then adds quantity to existing entry
    matched_items = False
    count = 0
    for item_entry in user_options.get_kart():

        if(item[0]['name'] == item_entry[0][0]['name']):

            sum = user_options.get_kart_subindex(count, 1) + quantity
            user_options.set_kart_index(count, item, sum)

            matched_items = True
            break

        count = count + 1

    if not matched_items:
        user_options.set_kart_new_item(item, quantity)


# This method checks player's kart for specified item; if item found
# then checks if quantity is greater than items in kart and will
# subtract accordingly. If items in kart reach 0 then item entry is
# removed from kart; if not found then player is notified item isn't
# in kart. 
def remove_item(user_options, item, quantity):
    matched_items = False
    count = 0
    for item_entry in user_options.get_kart():
        # print(item_entry)
        # print(item_entry[count]['name'])
        if(item[0]['name'] == item_entry[0][0]['name']):

            difference = 0

            if(CalculateEligibility. \
                determine_quantity_subtraction_eligibility( \
                    user_options.get_kart_subindex(count, 1), quantity)):
                difference = user_options.get_kart_subindex(count, 1) - quantity

                if(difference == 0):
                    user_options.remove_item_from_kart(count)

            matched_items = True
            # print(self.kart[count][1])
            user_options.set_kart_index(count, item, difference)
            break
        count = count + 1

    if not matched_items:
        print(f"\nSorry {user_options.get_name()}, we could not find " + \
              f"{item['name']} in your {user_options.get_kart_name()}")
    else:
        print(f"Removed {quantity}x {item[0]['name']} from kart")