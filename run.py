#!/usr/bin/env python
import sqlite3
from simulator import runSimulation
from drama import dramaticTyping

def fetchCoins():
    connection = sqlite3.connect('./currency_monitor.db')
    cursor = connection.cursor()
    query = "SELECT first_leg, ask FROM prices WHERE timestamp='1520408341.52' AND second_leg='USD';"
    cursor.execute(query)
    coinAskPrices = cursor.fetchall()
    coins = {}
    for coinAskPrice in coinAskPrices:
        if coinAskPrice[0] in coins:
            continue
        coins[coinAskPrice[0]] = {"price":coinAskPrice[1], "curreny":coinAskPrice[0]}
        dramaticTyping("{} - ${} \n".format(coinAskPrice[0], round(coinAskPrice[1],4)))
    return coins

def welcome():
    print("\n")
    dramaticTyping("Simple Crypto Trading Simulator \n")
    dramaticTyping("Hey Yo, you are back in time. It's Wednesday, March 7, 2018 7:39 AM \n")
    dramaticTyping("Here are the crypto currencies you can invest. \n")
    dramaticTyping("Fetching prices ... \n")


def inputBuy():
    dramaticTyping("Select the crypto curreny you want to buy? \n")
    curreny = raw_input("").upper()
    dramaticTyping("That's great. How much quantity you want to buy? \n")
    quantity = float(raw_input(""))
    return curreny, quantity

def quitMenu():
    dramaticTyping("Do you want to try again? Y/N ")
    answer = raw_input("").upper()
    if answer == 'Y':
        main()
    else:
        exit()

def main():
    welcome()
    coins = fetchCoins()
    currency, quantity = inputBuy()
    try:
        price = coins[currency]['price']
    except Exception as e:
        dramaticTyping("Invalid currency entered, please try again \n")
        inputBuy()
    runSimulation(coins[currency]['price'], quantity, currency)
    quitMenu()

main()
