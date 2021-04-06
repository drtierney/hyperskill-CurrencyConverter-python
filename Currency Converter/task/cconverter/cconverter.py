import requests


def get_currency_rates(currency_code):
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    r = requests.get(url)
    if r:
        print(r.json()['usd'])
        print(r.json()['eur'])
    else:
        print("Failed to get currency rates")


if __name__ == '__main__':
    my_code = input().lower()
    get_currency_rates(my_code)
