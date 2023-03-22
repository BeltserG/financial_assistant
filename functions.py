import re
import requests

def count_actions(list):
    numbers = []
    count = 1
    for i in list.keys():
        for x_ in list[i]:
            numbers.append(str(count))
            count+=1
    return numbers

def key_print():
    print("Press the key to take an action")

def get_the_key(keys):
    while True:
        try:
            action_number = input("Key: ")
            key = number_get_check(action_number, keys)
            break
        except ValueError:
            print("Invalid key. Please, try again.")
    print()
    return key

def number_get_check(number, numbers):
    str = "".join(numbers)
    if not re.search(f"[{str}]", number):
        raise ValueError
    else:
        return number

def ticker_info():
    while True:
        try:
            ticker = input("Enter stock ticker: ").strip().upper()
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=OSIV7VRPAC8U146L"
            r = requests.get(url)
            data = r.json()
            if not data["Global Quote"]:
                    raise KeyError
            list = []
            for i in data["Global Quote"].keys():
                    sublist = []
                    sublist.append(i.split(". ")[1])
                    sublist.append(data["Global Quote"][i])
                    list.append(sublist)
            return list
        except KeyError:
            print("No such stock. Please, try again")