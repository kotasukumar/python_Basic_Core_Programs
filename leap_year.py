def leap_year(year):

    if 999 < year < 10000:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    else:
        return "Invalid input,please enter a four digit number"


if __name__ == "__main__":
    year = int(input("Enter a year "))
    result = leap_year(year)
    print(result)