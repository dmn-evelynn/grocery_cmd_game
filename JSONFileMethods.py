# This file's purpose is to handle all of the file functions; creating and saving json file

import json

#"id": "", "name": "", "price": 
def create_aisle_file():
    #print("Creating File")
    aisles_data = {
        "aisles":[
            {
               "aisle_number": "1",
               "aisle_name": "Meat",
               "items":[
                   {"id": "101", "name": "ground beef", "price": 6.75, "weight": 3.00},
                   {"id": "102", "name": "chicken", "price": 5.50, "weight": 2.75},
                   {"id": "103", "name": "bacon", "price": 2.35, "weight": 1.05},
                   {"id": "104", "name": "turkey", "price": 8.00, "weight": 7.50}
                   ]
                },
            {
                "aisle_number": "2",
                "aisle_name": "Dairy",
                "items":[
                    {"id": "201", "name": "milk", "price": 2.15, "weight": 2.85},
                    {"id": "202", "name": "egg (x6)", "price": 2.65, "weight": 0.95},
                    {"id": "203", "name": "egg (x12)", "price": 4.15, "weight": 2.00},
                    {"id": "204", "name": "cheese", "price": 1.05, "weight": 1.00},
                    {"id": "205", "name": "butter", "price": 0.85, "weight": 0.50},
                    ]
                },
            {
                "aisle_number": "3",
                "aisle_name": "Produce",
                "items":[
                    {"id": "301", "name": "apple", "price": 2.20, "weight": 1.15},
                    {"id": "302", "name": "banana", "price": 0.95, "weight": 1.10},
                    {"id": "303", "name": "orange", "price": 1.75, "weight": 1.15},
                    {"id": "304", "name": "lettuce", "price": 1.50, "weight": 1.45}
                    ]
                },
            {
                "aisle_number": "4",
                "aisle_name": "Baking Needs",
                "items":[
                    {"id": "401", "name": "baking soda", "price": 3.15, "weight": 0.45},
                    {"id": "402", "name": "salt", "price": 1.05, "weight": 0.65},
                    {"id": "403", "name": "cooking oil", "price": .85, "weight": 1.05},
                    {"id": "404", "name": "mixing bowl set", "price": 5.75, "weight": 3.75}
                    ]
                },
            {
                "aisle_number": "5",
                "aisle_name": "Cleaning Supplies",
                "items":[
                    {"id": "501", "name": "paper towel", "price": 3.60, "weight": .85},
                    {"id": "502", "name": "bleach", "price": 4.00, "weight": 1.65},
                    {"id": "503", "name": "brush", "price": 2.50, "weight": 1.25},
                    {"id": "504", "name": "air refresher", "price": 3.15, "weight": 1.30}
                    ]
                }
            ]
        }
    
    with open("aisles.json", "w") as json_file:
        json.dump(aisles_data, json_file, indent=4)

#
# Read data in from file
#


def read_aisle_file():
    #print("Reading File")
    try:
        with open('aisles.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'data.json' not found. Please ensure the file exists.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'aisles.json'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
