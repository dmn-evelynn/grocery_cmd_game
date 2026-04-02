def select_item(aisle, aisle_number_input, user_info):
    print("This is the item selection screen. Choose an item id then the quantity.")
    while(True):
        item_id_input = input("\nDesired item id >>> ")

        matched_item_id = False
        item = ""

        for item in aisle['items']:
            if(item_id_input == item['id']):
                matched_item_id = True
                item_name = item['name']
                break
        
        if matched_item_id:
            while(True):
                input(f"Quantity of {item_name} >>> ")
                #=====
                #Continue Here :3
                #=====
                break

        else:
            print(f"\nSorry, {item_id_input} does not match any of the item ids in the aisle. Please try again!")
            