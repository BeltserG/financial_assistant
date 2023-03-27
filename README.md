# Financial Assistant

![](header_image.jpg)

## **Table of Contents**

1. [General information about the project](#general-information-about-the-project)
2. [Description of functions](#description-of-functions)
    1. [Stock screener](#1-stock-screener)
    2. [Portfolio manager](#2-portfolio-manager)
3. [Future additions](#future-additions)

## **Libraries Installation**

### Install libraries: 

    pip install -r requirements.txt

## **General information about the project**

Financial assistant is made to interract with the market data and manage your stock portfolio.

For current market data it uses free API from [www.alphavantage.co](http://www.alphavantage.co/). 

Portfolio is saved in the [CSV file](portfolio.csv)

To run the programm: 
    
    python project.py

In the following menu, select the desirable action:

    |         Menu          |       
    |:---------------------:|       
    |  Stock screener - 1   |       
    | Portfolio manager - 2 |       
    |       Quit - 3        |  
##  **Description of functions**
Due to the chosen action, you will be guided to the next section

## **1. Stock screener**

Stock screener allows you to get the current market data about a stock

    |  Stock screener  |
    |:----------------:|
    | Enter Ticker - 1 |
    |     Back - 2     |

To see information about the stock, enter the ticker.

<details> 
    <summary>Example with AAPL:</summary> 

    +--------------------+------------+
    | symbol             | AAPL       |
    | open               | 158.8600   |
    | high               | 160.3400   |
    | low                | 157.8500   |
    | price              | 160.2500   |
    | volume             | 59256343   |
    | latest trading day | 2023-03-24 |
    | previous close     | 158.9300   |
    | change             | 1.3200     |
    | change percent     | 0.8306%    |    

</details>

You can scan for another one or go to the main menu.

All algorithms work from `stock_screener.py` 
and some shared functions from `functions.py`

## **2. Portfolio manager**

Portfolio manager allows you to create/manage a portfolio.

    |     Portfolio manager     |
    |:-------------------------:|
    |    Show portfolio - 1     |
    |          Buy - 2          |
    |         Sell - 3          |
    | Remove whole position - 4 |
    |     Save & Return - 5     |
    | Return without saving - 6 |

### **1. Show**

You can show the portfolio in the format:

|   Ticker |   Current price, $ |   Average price, $ |   Ammount |   Total, $ |   Change, % |   Realized P\L, $ |
|---------:|-------------------:|-------------------:|----------:|-----------:|------------:|------------------:|
|     AMZN |              98.13 |                 95 |       100 |       9813 |        3.29 |                 0 |

### **2. Buy/Sell** 

You can add or reduce the positions with buy/sell actions.

You will be prompt to enter ticker, ammount in shares and price of the trade.

<details>
<summary>Example with adding ticker (AAPL), ammount (100), price (150):</summary>


Enter stock ticker: AAPL

Enter stock price: 150

Enter ammount of shares: 100
|   Ticker |   Current price, $ |   Average price, $ |   Ammount |   Total, $ |   Change, % |   Realized P\L, $ |
|---------:|-------------------:|-------------------:|----------:|-----------:|------------:|------------------:|
|     AMZN |              98.13 |                 95 |       100 |       9813 |        3.29 |                 0 |
|     AAPL |             160.25 |                150 |       100 |      15000 |        6.83 |                 0 |

</details>

### **3. Remove whole position**

You can remove the whole position from the portfolio.

### **4. Save & Return/Return without saving** 

You can quit to the main menu with/without saving

All algorithms work from `portfolio.py` 
and some shared functions from `functions.py`

## **Future additions**

[ ] GUI

[ ] Multiportfolio

[ ] Historical perfomance

[ ] Vs. Statistics

... and more features

### **May the compound interest be with You!**