import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv('ETH_INFURA_URL')
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def fetch_eth_transaction(tx_hash):
    tx = w3.eth.get_transaction(tx_hash)
    receipt = w3.eth.get_transaction_receipt(tx_hash)
    return {
        'hash': tx_hash,
        'from': tx['from'],
        'to': tx['to'],
        'gas': tx['gas'],
        'gasPrice': tx['gasPrice'],
        'value': tx['value'],
        'token_transfers': [
            {
                'from': log['address'],
                'topics': log['topics'],
                'data': log['data']
            } for log in receipt['logs']
        ]
    } 