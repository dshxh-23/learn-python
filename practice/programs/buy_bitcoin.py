import sys
import requests

try:
    n = float(sys.argv[1])

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=88957ebdc3d17b78e9ba24989afdde591261b86886eda0165956076cae07ae7e")
    obj = response.json()

    price = float((obj["data"])["priceUsd"])
    amt = price * n

    print(f"${amt:,.4f}")

except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    print("Invalid command line argument")