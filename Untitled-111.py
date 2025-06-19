class IntegerToRoman:
    def __init__(self):

        self.value_map = [
            (1000, 'M'), (900,  'CM'), (500, 'D'), (400, 'CD'),
            (100,  'C'), (90,   'XC'), (50,  'L'), (40,  'XL'),
            (10,   'X'), (9,    'IX'), (5,   'V'), (4,   'IV'),
            (1,    'I')
        ]

    def int_to_roman(self, num):
        if num <= 0:
            raise ValueError("Roman numerals exist only for positive integers.")
        roman_numeral = ""
        for value, symbol in self.value_map:

            count = num // value
            roman_numeral += symbol * count
            num -= value * count
        return roman_numeral


def main():
    try:
        n = int(input("Enter a positive integer: "))
        converter = IntegerToRoman()
        roman = converter.int_to_roman(n)
        print(f"The Roman numeral for {n} is {roman}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
