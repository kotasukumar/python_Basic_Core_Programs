def power_of_2(number):
    print("Enter the value of N")
    n = int(input())
    for i in range(n-1):
        number = number * 2

    print(number)


if __name__ == "__main__":
    power_of_2(2)