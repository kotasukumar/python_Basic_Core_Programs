def power_of_2(number,n):

    for i in range(n-1):
        number = number * 2

    return number


if __name__ == "__main__":
    n = int(input("Enter the value of N "))
    total_value = power_of_2(2,n)
    print(total_value)