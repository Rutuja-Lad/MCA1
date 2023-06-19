class CurrencyConverter:
    def __init__(self):
        self.conversion_rates = {
            "Euro": 0.01417,
            "British Pound": 0.0100,
            "Australian Dollar": 0.02140,
            "Canadian Dollar": 0.02027
        }

    def convert_to_currency(self, amount, currency):
        try:
            conversion_rate = self.conversion_rates[currency]
            converted_amount = amount / conversion_rate
            return round(converted_amount, 2)
        except KeyError:
            return -1


def main():
    converter = CurrencyConverter()

    # Prompt the user for input
    try:
        amount = float(input("Enter the amount needed in INR: "))
        currency = input("Enter the currency you have: ")
        converted_amount = converter.convert_to_currency(amount, currency)
        if converted_amount == -1:
            print("Invalid currency name. Please provide a valid currency.")
        else:
            print(f"The amount you should provide in {currency} is: {converted_amount}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

if __name__ == "__main__":
    main()