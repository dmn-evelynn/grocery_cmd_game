# This file's purpose is to display the selected aisle's information

def item_view_menu(aisles, user_input,user_info):
    for aisle in aisles['aisles']:
        if(user_input == aisle['aisle_number']):
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
            print(f"+{divider}+")
            for item in items:
                print(item)
            print(f"+{divider}+")