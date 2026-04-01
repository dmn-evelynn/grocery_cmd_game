# This file's purpose is to prompt user for name, starting funds, & kart preference

# This method adds values to the Customer object. Calls generate_wallet &
# generate_kart_preference which handle the wallet and kart preference.
def create_user(user_info):

    # Prompts user to enter name and then calls the set_name constructor. Afterwards,
    # the generate_wallet & generate_kart_preference methods are called.
    print("....Welcome.....erm, you seem unfamiliar. Tell me a little about yourself!")
    user_info.set_name(input("First Name >>> "), input("Last Name >>> "))
    print(f"\nHi, {user_info.first_name} {user_info.last_name}! " +
          "Welcome on in....tell me a little bit more about yourself!")

    generate_wallet(user_info)

    generate_kart_preference(user_info)


# This method prompts the user to enter their starting wallet funds. Rounds input
# to two decimal places.
def generate_wallet(user_info):
    while (True):
        try:
            user_input = input("Starting Funds (X.XX) >>> ")
            if 0.01 > float(user_input) >= 1000000.00:
                print(
                    "\nAck!...That is not a valid input....Enter between 0 & 1,000,000.00")
            else:
                user_info.set_wallet_funds(round(float(user_input), 2))
                print(user_info.wallet)
                break
        except ValueError:
            print("\nAck!...That is not a valid input....Enter between 0 & 1,000,000.00")


# This method prompts the user to enter their kart preference. Afterwards, the max
# weight limit will be calculated and added to the user_info object.
def generate_kart_preference(user_info):
    print("""\nPerfect...now which size kart is your preference? Chose one of the numbers below:

              [1] Handbasket (Can hold  30lbs)
              [2] Small-kart (Can hold  75lbs)
              [3] Large-kart (Can hold 125lbs)

              """)
    while (True):
        user_input = input("Kart Preference [1,2,3] >>> ")
        # print(user_input)
        # print(type(user_input))
        if not (user_input == "1" or user_input == "2" or user_input == "3"):
            print("""\nAck!...That is not a valid input....Enter 1, 2, or 3:

              [1] Handbasket (Can hold  30lbs)
              [2] Small-kart (Can hold  75lbs)
              [3] Large-kart (Can hold 125lbs)

              """)
        else:
            user_info.set_kart_preference(user_input)
            break
