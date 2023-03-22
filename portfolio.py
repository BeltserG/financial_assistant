import functions
import csv
import os
import requests
from tabulate import tabulate


def main():
    portfolio_manager_menu()

def portfolio_manager_menu():
    portfolio = Portfolio("portfolio.csv")
    return portfolio_init(portfolio)
     
def portfolio_init(p):
    menu_content = {
    "Portfolio manager" : ["Show portfolio - 1", "Buy - 2", "Sell - 3", "Remove whole position - 4", "Save & Return - 5", "Return without saving - 6"]
    }
    print((tabulate(menu_content, headers="keys", tablefmt="pipe", stralign="center")) + "\n")
    actions = functions.count_actions(menu_content)
    functions.key_print()
    key = functions.get_the_key(actions)
    return (navigate_from_portfolio_manager(key, p))

def navigate_from_portfolio_manager(action, p):
    match action:
        case "1":
            os.system("cls")
            p.show()
            print("\n" + "*"*29 + "\n")
            portfolio_init(p)
        case "2":
            os.system("cls")
            add(p)        
        case "3":
            os.system("cls")
            trim(p)
        case "4":
            os.system("cls")
            delete(p)
        case "5":
            p.reload()
            os.system("cls")
            return 0
        case "6":
            os.system("cls")
            return 0
            
def add(p):
    list = prompt_for_trade()
    p.buy(*list)
    p.show()
    print("Press 1 to add more\nPress 2 to return to menu")
    key = functions.get_the_key(["1","2"])
    if key == "1":
        add(p)
    elif key == "2":
        portfolio_init(p) 

def trim(p):
    list = prompt_for_trade()
    p.sell(*list)
    p.show()
    print("Press 1 to remove more\nPress 2 to return to menu")
    key = functions.get_the_key(["1","2"])
    if key == "1":
        trim(p)
    elif key == "2":
        portfolio_init(p)       

def delete(p):
    ticker = input("Enter ticker: ").strip().upper()
    p.remove(ticker)
    print("Press 1 to remove another one\nPress 2 to return to menu")
    key = functions.get_the_key(["1","2"])
    if key == "1":
        delete(p)
    elif key == "2":
        portfolio_init(p) 

class Portfolio:
    def __init__(self, filename):
        self.headers = ["Ticker", "Current price, $", "Average price, $", "Ammount", "Total, $", "Change, %", "Realized P\L, $"]
        self.positions = []
        self.set_portfolio(filename)
    
    def set_portfolio(self, file):
        try:
            with open(file) as f:
                portfolio_file = csv.DictReader(f)
                for row in portfolio_file:
                    today_data = self.get_ticker_info(row["Ticker"])
                    current_price = float(today_data[4][1])
                    self.positions.append({"Ticker": row["Ticker"],
                                           "Current price, $": round(float(current_price), 2),
                                           "Average price, $": float(row["Average price, $"]), 
                                           "Ammount": int(row["Ammount"]),
                                           "Total, $": round(float(current_price*int(row["Ammount"])), 2),
                                           "Change, %": round(float(((current_price/float(row["Average price, $"]))-1)*100),2),
                                           "Realized P\L, $": float(row["Realized P\L, $"])})
        except FileNotFoundError:
            with open(file, "w") as f:
                writer = csv.writer(f)
                writer.writerow(self.headers)
    def get_ticker_info(self, ticker):
        while True:
            try:
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
                pass
    def show(self):
        print(tabulate(self.positions, headers="keys", tablefmt="pipe", stralign="right"))
    
    def reload(self):
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(self.positions)

    def buy(self, ticker, price, ammount):
        found = False
        for i in self.positions:
            if i["Ticker"] == ticker:
                old_ammount = int(i["Ammount"])
                old_price = float(i["Average price, $"])
                i["Average price, $"] = round(((old_price * old_ammount) + (price) * (ammount)) / (old_ammount + ammount), 2)
                i["Ammount"] = old_ammount + ammount
                i["Total, $"] = round(i["Current price, $"] * i["Ammount"], 2)
                i["Change, %"] = round((i["Total, $"]/(i["Average price, $"]*i["Ammount"])- 1)*100, 2)
                found = True
                break
        if not found:
            today_data = self.get_ticker_info(ticker)
            current_price = today_data[4][1]
            self.positions.append({"Ticker": ticker,
                                    "Current price, $": round(float(current_price), 2),
                                    "Average price, $": price, 
                                    "Ammount": ammount,
                                    "Total, $": float(price*ammount),
                                    "Change, %": round(float((float(current_price)/price - 1)*100), 2),
                                    "Realized P\L, $": float(0)})
    
    def sell(self, ticker, price, ammount):
        found = False
        for i in self.positions:
            if i["Ticker"] == ticker:
                if ammount == i["Ammount"]:
                    i["Ammount"] = 0
                    i["Total, $"] = float(0)
                    i["Change, %"] = float(0)
                    i["Realized P\L, $"] = round(float((price - i["Average price, $"])*ammount), 2)
                    i["Average price, $"] = float(0)
                    print(f"--{ticker} edited--")
                    break
                elif ammount > i["Ammount"]:
                    print("Given ammount exceeds ammount in portfolio")
                    break
                else:
                    old_ammount = int(i["Ammount"])
                    i["Ammount"] = old_ammount - ammount
                    i["Total, $"] = round(i["Current price, $"] * i["Ammount"], 2)
                    i["Realized P\L, $"] = round(float((price - i["Average price, $"])*ammount), 2)
                    found = True
                    print(f"--{ticker} edited--")
                    break
        if not found:
            print("No position with that ticker")
    
    def remove(self, ticker):
        found = False
        for i in self.positions:
            if i["Ticker"] == ticker:
                self.positions.remove(i)
                found = True
                self.show()
                print(f"--{ticker} is deleted--")
                break
        if not found:
            print("No position with that ticker")

                               
def prompt_for_trade():
    while True:
        try:
            ticker = input("Enter stock ticker: ").strip().upper()
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=OSIV7VRPAC8U146L"
            r = requests.get(url)
            data = r.json()
            if not data["Global Quote"]:
                    raise KeyError
            break
        except KeyError:
            print("No such stock. Please, try again")
    price = float(input("Enter stock price: ").strip())
    ammount = int(input("Enter ammount of shares: ").strip())
    return [ticker,price,ammount]

if __name__ == "__main__":
     main()     