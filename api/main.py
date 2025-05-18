from fastapi import FastAPI, HTTPException
from db.redis_cache import get_cached_transaction
from analytics.gas_fees import compute_gas_fee_trend
from analytics.token_movement import compute_token_movement
from analytics.arbitrage import detect_arbitrage_opportunities
from .schemas import TransactionSchema, GasFeeTrendResponse, TokenMovementResponse, ArbitrageOpportunity

app = FastAPI()

@app.get('/transaction/{tx_hash}', response_model=TransactionSchema)
def get_transaction(tx_hash: str):
    tx = get_cached_transaction(tx_hash)
    if not tx:
        raise HTTPException(status_code=404, detail='Transaction not found')
    return tx

@app.get('/analytics/gas-fee', response_model=GasFeeTrendResponse)
def gas_fee_trend(chain: str, window: str = '1h'):
    # Stub: fetch transactions from DB for the chain and window
    transactions = []
    return compute_gas_fee_trend(transactions, window)

@app.get('/analytics/token-movement', response_model=list[TokenMovementResponse])
def token_movement(chain: str):
    # Stub: fetch transactions from DB for the chain
    transactions = []
    top_tokens = compute_token_movement(transactions)
    return [TokenMovementResponse(token=t[0], volume=t[1]) for t in top_tokens]

@app.get('/analytics/arbitrage', response_model=list[ArbitrageOpportunity])
def arbitrage_opportunities():
    # Stub: fetch cross-chain transactions
    transactions = []
    return detect_arbitrage_opportunities(transactions) 