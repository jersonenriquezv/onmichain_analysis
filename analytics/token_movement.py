def compute_token_movement(transactions):
    # transactions: list of dicts with 'token_transfers'
    # Stub: implement aggregation logic here
    token_volumes = {}
    for tx in transactions:
        for transfer in tx.get('token_transfers', []):
            token = transfer.get('token', 'UNKNOWN')
            amount = transfer.get('amount', 0)
            token_volumes[token] = token_volumes.get(token, 0) + amount
    top_tokens = sorted(token_volumes.items(), key=lambda x: x[1], reverse=True)
    return top_tokens 