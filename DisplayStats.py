# This file's purpose is to display the user's stats

# This method prints out the customer's stats along with a special first time message
def display_stats(user_info):
    breaker = '-~-' * 10
    first_visit = True

    if first_visit:
        print("\n...Let us take a look at your stats:")
        first_visit = False
    else:
        print("\nCustomer Stats:")

    print(breaker + "\n" +
          f"First Name       | {user_info.first_name}\n" +
          f"Last Name        | {user_info.last_name}\n" +
          f"Wallet           | {user_info.wallet:.2f}\n" +
          f"Weight Limit     | {user_info.weight_limit:.2f}\n" +
          f"Remaining Weight | {user_info.remaining_weight:.2f}\n" +
          breaker)
