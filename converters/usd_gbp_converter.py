from converters.currency_converter import CurrencyConverter


class UsdGbpConverter(CurrencyConverter):
    def __init__(self, rate):
        self.rate = rate

    def convert(self, amount):
        return amount * self.rate
