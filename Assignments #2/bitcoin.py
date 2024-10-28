import sys
import requests

def main():

    try:
        # String to float of n bitcoins
        n = float(sys.argv[1])

        # Get bitcoin exchange rate
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        price = requests.get(url)
        data = price.json()
        n_price = data["bpi"]["USD"]["rate_float"]

        # Get the total amount in USD for n bitcoin
        amount = n * n_price
        print(f"${amount:,.4f}")

    # Exit the program if an error occurs
    except requests.RequestException:
        sys.exit()

main()