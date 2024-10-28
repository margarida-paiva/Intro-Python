import sys

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    total = 0

    while True:
        try:

            # Prompt the user for an item and standardize input to title case
            item = input("Item: ").title()

             # Check if item is in the menu
            if item in menu:

                 # Give the total (formatted)
                total += menu[item]
                print(f"Total: ${total:.2f}")

        # Exit the program if the user inputs control-d
        except EOFError:
            sys.exit()

main()