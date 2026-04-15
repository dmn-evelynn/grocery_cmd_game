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
          f"Name             | {user_info.get_name()}\n" +
          f"Wallet           | {user_info.get_wallet():.2f}\n" +
          f"Weight Limit     | {user_info.get_weight_limit():.2f}\n" +
          f"Remaining Weight | {user_info.get_remaining_weight():.2f}\n" +
          breaker)

    user_info.display_kart()


def print_related_stats(user_info):
    wallet_display =           f"| Funds:            {user_info.get_wallet():.2f}"
    remaining_weight_display = f"| Remaining Weight: {user_info.get_remaining_weight():.2f}"
    
    highest_length = len(wallet_display)
    if highest_length < len(remaining_weight_display):
        highest_length = len(remaining_weight_display)
        spacing = ' ' * (highest_length - len(wallet_display))
        wallet_display += spacing
    else:
        spacing = ' ' * (highest_length - len(remaining_weight_display))
        remaining_weight_display += spacing

    wallet_display += " |\n"
    remaining_weight_display += " |\n"
        
    
    divider_length = ((len(wallet_display) + len(remaining_weight_display) - 5) // 2) * '='
    divider = f"+{divider_length}+"

    print(wallet_display + remaining_weight_display + divider)