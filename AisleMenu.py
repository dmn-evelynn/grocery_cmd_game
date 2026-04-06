# This file's purpose is to prompt the user for their aisle selection

import JSONFileMethods, Checkout, DisplayAisle, ItemSelectionMenu

# This method allows the user to chose an aisle, learn more about each aisle, or
# return to the main menu.
def enter_aisles(user_info):
    create_file = True
    if (create_file):
        JSONFileMethods.create_aisle_file()
        create_file = False
        
    
        
    print("""\nWhich aisle will you go to? Choose from the following:

        [1] Meat
        [2] Dairy
        [3] Fauna
        [4] Baking Needs
        [5] Cleaning Supplies
        [6] Display kart
        [7] Checkout
        [8] Back to Main Menu\n""")
    user_input = input("Your selection >>> ")

    while (True):
        break_out_while = False
        if not (user_input == "1" or user_input == "2" or user_input == "3" or \
            user_input == "4" or user_input == "5" or user_input == "6" or \
            user_input == "7" or user_input == "8"):
            print("""\nAck!...That is not a valid input....Enter 1, 2, 3, 4, 5, 6, 7, or 8:

        [1] Meat
        [2] Dairy
        [3] Fauna
        [4] Baking Needs
        [5] Cleaning Supplies
        [6] Display kart
        [7] Checkout
        [8] Back to Main Menu\n""")
            user_input = input("Your selection >>> ")
            
        else:
            
            match user_input:
                case "1" | "2" | "3" | "4" | "5":
                    #run thru methods
                    aisles = JSONFileMethods.read_aisle_file()
                    selected_aisle = DisplayAisle.item_view_menu(aisles, user_input, user_info)
                    is_item_selected = ItemSelectionMenu.select_item(selected_aisle['items'], user_info, "add")

                    if is_item_selected:                 
                        break_out_while = True
                    #return to previous menu
                    break
                case "6":
                    user_info.display_kart()
                    break
                case "7":
                    Checkout.checkout(user_info)
                    break_out_while = True
                    break
                case "8":
                    break_out_while = True
                    break
                
            if(break_out_while):
                break
            
        
    # Aisle Layout ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Aisle 1 -     Meat (ground beef, chicken, bacon, turkey)
    # Aisle 2 -    Dairy (milk, eggs, cheese, butter)
    # Aisle 3 -    Fauna (lettuce, apples, oranges, bananas)
    # Aisle 4 -   Baking (baking soda, salt, oil, bowls)
    # Aisle 5 - Cleaning (paper towel, bleach, brush, air refresher)
    # Checkout
    # Quit
