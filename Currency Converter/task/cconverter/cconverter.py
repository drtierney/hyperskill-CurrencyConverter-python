
currencies = {
    'RUB': {'name': 'Russian Ruble', 'rate': 2.98},
    'ARS': {'name': 'Argentine Peso', 'rate': 0.82},
    'HNL': {'name': 'Honduran Lempira', 'rate': 0.17},
    'AUD': {'name': 'Australian Dollar', 'rate': 1.9622},
    'MAD': {'name': 'Moroccan Dirham', 'rate': 0.208},
}


def conicoin_rates(**currency_dict):
    conicoins = float(input())

    for code in currencies.keys():
        amount = conicoins * currencies[code]['rate']
        print(f"I will get {round(amount, 2)} {code} from the sale of {conicoins} conicoins.")


if __name__ == '__main__':
    conicoin_rates(**currencies)
