#!/usr/bin/env python

import sqlite3
from drama import dramaticTyping
import datetime

def fetchLastBidPriceFromDB(currency):
    connection = sqlite3.connect('./currency_monitor.db')
    cursor = connection.cursor()
    query = "SELECT max(bid),timestamp from prices WHERE first_leg='{}' and second_leg='USD' and timestamp> '1520408341.52'".format(currency)
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows[0], rows[1]


def runSimulation(boughtPrice, quantity, currency):
    valueThen = boughtPrice * quantity
    bestPrice, timestamp = fetchLastBidPriceFromDB(currency)
    valueNow = bestPrice * quantity
    priceDifference = (valueNow - valueThen)/float(valueThen) * 100
    time = datetime.datetime.fromtimestamp(timestamp).strftime('%A, %B %-d, %Y %I:%M %p')
    dramaticTyping("The best bid price for {} was ${} at {} \n".format(currency, bestPrice, time))
    if priceDifference>0:
        dramaticTyping("Your total asset value is ${}, it has increase by {}% \n".format(round(valueNow, 4), round(priceDifference,2)))
    else:
        dramaticTyping("Your total asset value is ${}, it has decreased by {} \n".format(round(valueNow, 4), round(priceDifference,2)))
