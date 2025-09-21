# imports
import requests # requests
import sys # sys
import json # JSON or JavaScript Object Notation

# if length of cmnd-line args < 2
if len(sys.argv) != 2:
    # exit
    sys.exit("Invalid number of command-line arguments.")

# try block
try:
    # n = float of 2nd item in cmd-line args
    n = float(sys.argv[1])

    # def api key and link
    API_KEY = "9df74c7c2b3aa6660d0e9450b734da299a1e0c24564e0c9c13a6e1d9884bde8c"
    link = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"

    # try block
    try:
        # make request from API using link
        response = requests.get(link).json()
    # except for request exception
    except requests.RequestException:
        # exit
        sys.exit("Whoops! Something went wrong. Try again later.")

    # grab price per coin
    ppc = response["data"]["priceUsd"]

    # price per coin * n coins
    price = float(ppc)*float(n)
    print(f'${price:,.4f}')

# except value error
except ValueError:
    # exit
    sys.exit("Invalid command-line argument.")
