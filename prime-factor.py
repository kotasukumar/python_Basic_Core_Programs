def prime_factor():
    print("Enter any number")
    number = int(input())

    while number%2 == 0:
        print("2")
        number = int(number / 2)

    j = 3
    for i in range(int(number/2)):
            while number%j == 0:
                print(j)
                number = int(number / j)

    if number > 2:
        print(number)


if __name__ == "__main__":
    prime_factor()