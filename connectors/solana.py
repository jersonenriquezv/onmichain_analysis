import os
from solana.rpc.api import Client
from dotenv import load_dotenv

load_dotenv()

SOLANA_RPC_URL = os.getenv('SOLANA_RPC_URL')
client = Client(SOLANA_RPC_URL)

def fetch_solana_transaction(tx_sig):
    resp = client.get_transaction(tx_sig, encoding='json')
    if not resp['result']:
        return None
    tx = resp['result']
    meta = tx['meta']
    message = tx['transaction']['message']
    return {
        'hash': tx_sig,
        'from': message['accountKeys'][0],
        'to': message['accountKeys'][1] if len(message['accountKeys']) > 1 else None,
        'fee': meta['fee'],
        'token_transfers': meta.get('postTokenBalances', [])
    } 