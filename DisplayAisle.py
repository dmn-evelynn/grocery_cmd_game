# This file's purpose is to display the selected aisle's information

def item_view_menu(aisles, user_input, user_info):
    selected_aisle = ""
    for aisle in aisles['aisles']:
        try:
            aisle_number = int(aisle['aisle_number'])
        except ValueError:
            print("...Error...Aisle number could not be set to an integer.")
        if(user_input == aisle_number):
            #print(f"Match\t{user_input}\t{aisle['aisle_name']}")
            
            items = []
            highest_line_length = 0
            highest_item_length = 0

            for item in aisle['items']:
                if highest_item_length < len(item['name']):
                    highest_item_length = len(item['name'])

            for item in aisle['items']:
                spacing = ' ' * (highest_item_length - len(item['name']))
                
                line = f"| item id | {item['id']} ||  || item name | {item['name']}{spacing} ||  || item price | {item['price']:.2f} ||  || item weight | {item['weight']:.2f} |"
                
                items.append(line)
                
                if highest_line_length < len(line):
                    highest_line_length = len(line)

            divider = '=' * (highest_line_length - 2)
            print(f"\n\t-~= {aisle['aisle_name']} =~-")
            print(f"+{divider}+")
            for item in items:
                print(item)
            print(f"+{divider}+\n")

            selected_aisle = aisle
    return selected_aisle