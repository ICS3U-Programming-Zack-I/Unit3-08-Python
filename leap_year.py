#!/usr/bin/env python3
# Created by: Zack Isingoma
# Created on: 16th december 2021

def main():
    year_as_string = input("Enter the year: ")
    try:
        year_as_int = int(year_as_string)
        if (year_as_int % 4) == 0:
            if (year_as_int % 100) == 0:
                if (year_as_int % 400) == 0:
                    print("{} is a leap year".format(year_as_int))
                else:
                    print("{} is not a leap year".format(year_as_int))
            else:
                print("{} is a leap year".format(year_as_int))
        else:
            print("{} is not a leap year".format(year_as_int))
    except Exception:
        print("This input was invalid")
    finally:
        print("Thank you for your participation ")


if __name__ == "__main__":
    main()
