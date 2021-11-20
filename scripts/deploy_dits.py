import time

from scripts import chain_functions
from brownie import Ditcoin, network, config, TokenERC20

initial_supply = 1000000000000000000000
token_name = "DitCoin"
token_symbol = "DTC"

def deploy_ditcoin():
    account = chain_functions.get_account(id="eth_metamask")
    # account = chain_functions.get_account()
    net = network.show_active()
    print(f"=================NETWORK=================\n{net}\n========================================")
    
    
    
    
    ditcoin = Ditcoin.deploy(
        chain_functions.get_contract("eth_usd_price_feed").address,# constructor of lottery.sol "priceFeedAddress"
        chain_functions.get_contract("link_token").address, # the chainlink token...
        config['networks'][network.show_active()]['fee'], # get the preset ones in brownie-config
        config['networks'][network.show_active()]['keyhash'],
        {"from":account},
        publish_source=config['networks'][network.show_active()].get('verify', False) # get the verify key - but if this isnt set, set this to False
    )
    print(f"Lottery contract address: {Ditcoin[-1]}")
    
    return ditcoin 
    

def main():
    deploy_ditcoin()
    