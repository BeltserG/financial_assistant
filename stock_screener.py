from tabulate import tabulate
import functions
import os

def main():
      stock_screener_menu()

def stock_screener_menu():
       menu_content = {
       "Stock screener" : ["Enter Ticker - 1", "Back - 2"]
       }
       print(tabulate(menu_content, headers="keys", tablefmt="pipe", stralign="center"))
       actions = functions.count_actions(menu_content)
       functions.key_print()
       key = functions.get_the_key(actions)
       return (navigate_from_stock_screener(key))

def navigate_from_stock_screener(action):
       match action:
            case "1":
                   os.system("cls")
                   get_ticker_info()
                   return 0
            case "2":
                   os.system("cls")
                   return 0

def get_ticker_info():
       list = functions.ticker_info()
       print(tabulate(list, tablefmt="psql"))
       print("Press 1 to scan for another one\nPress 2 to return to menu")
       key = functions.get_the_key(["1","2"])
       if key == "1":
              os.system("cls")
              get_ticker_info()
       elif key == "2":
              os.system("cls")
              return 0
                                        
if __name__ == "__main__":
    main()