#!/usr/bin/python3

"""This module represent a currency converter"""

base_rate_dict =  {"GHS": 13, "NGN": 1306.67, "KN": 14}
result = 0

def converter(base, quote, amount):
    if base != "USD" and quote != "USD":
        result = (amount / base_rate_dict[base]) * base_rate_dict[quote]
    elif base == "USD":
        result = amount * base_rate_dict[quote]
    elif quote == "USD":
        result = amount / base_rate_dict[base]
    else:
        result = 0
    print(f"Value: {quote}{result}")

def main():
    base_curr = input("Enter the currency you want to convert from: ")
    quote_curr = input("Enter the Currency you want to convert to: ")
    amount = int(input("Enter the amount you want to convert: ")) 
    converter(base_curr, quote_curr, amount)

main()
