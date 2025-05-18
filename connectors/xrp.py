import os
from xrpl.clients import JsonRpcClient
from xrpl.models.requests import Tx
from dotenv import load_dotenv

load_dotenv()

XRP_RPC_URL = os.getenv('XRP_RPC_URL')
client = JsonRpcClient(XRP_RPC_URL)

def fetch_xrp_transaction(tx_hash):
    req = Tx(transaction=tx_hash)
    resp = client.request(req)
    tx = resp.result
    return {
        'hash': tx_hash,
        'from': tx.get('Account'),
        'to': tx.get('Destination'),
        'fee': tx.get('Fee'),
        'token_transfers': tx.get('Memos', [])
    } 