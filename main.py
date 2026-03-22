from converters import UsdRubConverter, UsdEurConverter, UsdGbpConverter, UsdCnyConverter
from converters import get_rates


def main():
    amount = int(input('Введите значение в USD: \n'))

    rates = get_rates()

    converter = UsdRubConverter(rates['RUB'])
    print(f"{amount} USD to RUB: {converter.convert(amount)}")

    converter = UsdEurConverter(rates['EUR'])
    print(f"{amount} USD to EUR: {converter.convert(amount)}")

    converter = UsdGbpConverter(rates['GBP'])
    print(f"{amount} USD to GBP: {converter.convert(amount)}")

    converter = UsdCnyConverter(rates['CNY'])
    print(f"{amount} USD to CNY: {converter.convert(amount)}")


if __name__ == "__main__":
    main()
