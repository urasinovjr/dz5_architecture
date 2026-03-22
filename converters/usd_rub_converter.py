from converters.currency_converter import CurrencyConverter


class UsdRubConverter(CurrencyConverter):
    def __init__(self, rate):
        self.rate = rate

    def convert(self, amount):
        return amount * self.rate
