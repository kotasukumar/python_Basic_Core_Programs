def harmonic():
    print("Enter the value of n")
    n = int(input())
    number = 1.0
    number1 = 1

    for i in range(n-1):
        number1 = number1 + (1/(number+1))
        number = number + 1
    print(number1)


if __name__ == "__main__":
    harmonic()