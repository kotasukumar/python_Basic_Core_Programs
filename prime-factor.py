def prime_factor(number):
    prime_factor = []

    j = 2
    for i in range(number // 2):
            while number % j == 0:
                print(j)
                number = int(number / j)
            j += 1

    if number > 2:
        print(number)


if __name__ == "__main__":
    number = int(input("Enter any number: "))
    prime_factor(number)