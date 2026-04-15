# This file's purpose is to prompt the user for their aisle selection

import JSONFileMethods, Checkout, DisplayAisle, ItemSelectionMenu


file_created = True
print_header = True

JSONFileMethods.create_file()
aisles = JSONFileMethods.read_aisle_file()
filtered_aisles = aisles['aisles']

header = "\nWhich aisle will you go to? Choose from the following by inputting an integer:"
error_msg = f"\nAck!...That is not a valid input....Enter 1 - {len(filtered_aisles) + 3}:"

user_input = ""

# This method takes in a user_info object; global variables are set for aisles,
# filtered_aisles, header, error_msg, & user_input. Create_file() method is
# called; Infinite while loop that prints out either a header or error
# message along with selectable options; User is prompted for an integer; This
# value is error checked and then is checked for dynamic and predetermined 
# options. 
def enter_aisles(user_info):
    global aisles, filtered_aisles, header, error_msg, user_input, print_header
        
    while True:
        if print_header:
            print(header)
        else:
            print(error_msg)
            print_header = True

        print_options(filtered_aisles)

        try:
            user_input = int(input("\nYour selection >>> ").strip())
        except ValueError:
            print_header = False
            continue

        if user_input == len(filtered_aisles) + 3:
            break
        
        if user_input == len(filtered_aisles) + 2:
            Checkout.checkout(user_info)
            break

        if user_input == len(filtered_aisles) + 1:
            user_info.display_kart()
            continue

        if user_input in range(1, len(filtered_aisles)):
            selected_aisle = DisplayAisle.item_view_menu(aisles, user_input, user_info)
            is_item_selected = ItemSelectionMenu.select_item(selected_aisle['items'], user_info, "add")
            continue
        
        print_header = False     
        

# This method takes in an aisles list that contains information about an unknown 
# amount of aisles; It takes this information and prints out a numbered list of
# choices with the names of the aisles, a display kart option, a checkout option
# and a back to Main Menu option. 
def print_options(aisles):
    for i, aisle in enumerate(aisles, start=1):
        print(f"\t[{i}] {aisle['aisle_name']}")
    print(f"\t[{len(aisles) + 1}] Display Kart")
    print(f"\t[{len(aisles) + 2}] Checkout")
    print(f"\t[{len(aisles) + 3}] Back to Main Menu")