# This file manages methods for adding and removing items from the player's kart.
import CalculateEligibility, ItemSelectionMenu

# This method checks the player's kart for alike items and then adds new quantity
# to existing quantity; if alike items are not found then a new entry it made.
def add_item(self, item, quantity):
    # Method that searches kart list for same item entry; then adds quantity to existing entry
    matched_items = False
    count = 0
    for item_entry in self.kart:
        # print(item_entry)
        # print(item_entry[count]['name'])
        if(item['name'] == item_entry[count]['name']):
            # print(self.kart[count])
            sum = self.kart[count][1] + quantity
            # print(f"\n{self.kart[count][1]}\n\n{sum}")
            self.kart[count] = (item, sum)
            # print(item_entry, (self.kart[count][1] + quantity))
            matched_items = True
            break
        count = count + 1

    if not matched_items:
        self.kart.append((item, quantity))


# This method checks player's kart for specified item; if item found
# then checks if quantity is greater than items in kart and will
# subtract accordingly. If items in kart reach 0 then item entry is
# removed from kart; if not found then player is notified item isn't
# in kart. 
def remove_item(self, item, quantity):
    matched_items = False
    count = 0
    for item_entry in self.kart:
        # print(item_entry)
        # print(item_entry[count]['name'])
        if(item['name'] == item_entry[count]['name']):

            if(CalculateEligibility.determine_quantity_subtraction_eligibility(self.kart[count][1], quantity)):
                difference = self.kart[count][1] - quantity

                if(difference == 0):
                    del self.kart[count]

            matched_items = True
            break
        count = count + 1

    if not matched_items:
        print(f"\nSorry {self.name}, we could not find {item['name']} in your {self.get_kart_name}")
    else:
        print(f"Removed {quantity}x {item['name']} from kart")