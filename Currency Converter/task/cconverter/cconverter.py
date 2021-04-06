import requests


def convert_currency(value, rate):
    return round(value * rate, 2)


def get_currency_rates(currency_code):
    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    r = requests.get(url).json()

    if currency_code != 'usd':
        currencies_cache['usd'] = float(r['usd']['rate'])
    if currency_code != 'eur':
        currencies_cache['eur'] = float(r['eur']['rate'])

    while True:
        request_code = input().lower()
        if request_code == '':
            break
        amount = int(input())
        print("Checking the cache...")
        request_rate = float(r[request_code]['rate'])
        if request_code in currencies_cache.keys():
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            currencies_cache[request_code] = request_rate
        print(f"You received {convert_currency(amount, request_rate)} {request_code.upper()}")


if __name__ == '__main__':
    currencies_cache = {}
    my_code = input().lower()
    get_currency_rates(my_code)
