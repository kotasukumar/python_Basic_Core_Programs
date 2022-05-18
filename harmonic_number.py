def harmonic(n):

    number = 1.0
    total_value = 1

    for i in range(n-1):
        total_value = total_value + (1 / number + 1)
        number = number + 1
    return total_value


if __name__ == "__main__":
    n = int(input("Enter the value of n "))
    value = harmonic(n)
    print(value)