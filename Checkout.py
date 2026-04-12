# This file's purpose is to handle the checkout portion of the game;
# Having light conversation between user and employee; employee
# gives different responses per answer

def checkout(user_info):
    if user_info.kart == []:
        print(f"\n...Oops, apologies {user_info.name}...You " \
            "need to add some items to your kart!...")
    else:
        print("Checking out...")
