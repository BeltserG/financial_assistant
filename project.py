import sys
import functions
import os
from tabulate import tabulate
from stock_screener import stock_screener_menu
from portfolio import portfolio_manager_menu

def main():
    os.system("cls")
    menu_content = {
        "Menu" : ["Stock screener - 1", "Portfolio manager - 2", "Quit - 3"],
        }
    actions = count_actions(menu_content)
    main_menu(menu_content)
    key_print()
    key = functions.get_the_key(actions)
    navigate_from_main(key)
   
def main_menu(content):
    print("-"*25)
    print(" "*10 + "Hello!")
    print("-"*25)
    print("Here is your financial assistant\n")
    print(tabulate(content, headers="keys", tablefmt="pipe", stralign="center"))

def navigate_from_main(action):
    match action:
        case "1":
            os.system("cls")
            x = stock_screener_menu()
            if x == 0:
                main()
        case "2":
            os.system("cls")
            x = portfolio_manager_menu()
            if x == 0:
                main()
        case "3":
            os.system("cls")
            sys.exit("May the power of compound interest be with You!")
            
def count_actions(list):
    numbers = []
    count = 1
    for i in list.keys():
        for x in list[i]:
            numbers.append(str(count))
            count+=1
    return numbers

def key_print():
    print("\nPress the key to take an action\n")

if __name__ == "__main__" :
    main()