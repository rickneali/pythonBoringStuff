# The Collatz Sequence


def collatz():
    number = int(input("Enter number: "))
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1

        print(int(number))


collatz()
