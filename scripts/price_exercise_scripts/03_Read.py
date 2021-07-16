#!/usr/bin/python3
from brownie import PriceExercise


def main():
    price_contract = PriceExercise[-1]
    print("Reading data from {}".format(price_contract.address))
    if price_contract.price() == 0:
        print(
            "You may have to wait a minute and then call this again, unless on a local chain!"
        )
    print("Feed Price: {}".format(price_contract.getLatestPrice()))
    print("API Price: {}".format(price_contract.price()))
    print("Feed > API : {}".format(price_contract.priceFeedGreater()))