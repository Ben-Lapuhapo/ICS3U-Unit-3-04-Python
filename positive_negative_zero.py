#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: October 1 2019
# This program reads an integer and displays the sign (+ or -)


def main():
    # Input
    number = input("Input a Number: ")
    print("")

    # Process and Output
    if number == "0":
        print("Neutral Number:", number)
    elif number > "5":
        print("Negative Number: -", number)
    elif number < "6":
        print("Positive Number: +", number)
    else:
        print("No idea!")


if __name__ == "__main__":
    main()
