class Reverse:
    def __init__(self, s=""):
        """
        Constructor with a default string value.
        If no argument is passed, s will be an empty string.
        """
        self.s = s

    def get_reversed(self):
        """
        Returns the reversed version of the string stored in self.s.
        """
        return self.s[::-1]


def main():

    user_input = input("Enter a word to reverse: ")

    reverser = Reverse(user_input)

    print("Reversed string:", reverser.get_reversed())


if __name__ == "__main__":
    main()
