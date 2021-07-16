#!/usr/bin/python3
from brownie import PriceExercise, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)
from scripts.deploy_mocks import deploy_mocks


def deploy_price_exercise():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(MockOracle) <= 0:
            deploy_mocks()
        oracle = MockOracle[-1].address
        link_token = LinkToken[-1].address
        price_feed = MockV3Aggregator[-1].address
    else:
        oracle = get_contract("oracle").address
        link_token = get_contract("link_token").address
        price_feed = get_contract("btc_usd_price_feed").address
    
    price_exercise = PriceExercise.deploy(
        price_feed, 
        oracle, 
        jobId, 
        fee,
        link_token, 
        {"from": account},
        publish_source= get_verify_status(),
    )
    print(f"PriceExercise deployed to {price_exercise.address}")
    return price_exercise

def main():
    deploy_price_exercise()
