from .consumer import consume_transactions
from .producer import send_transaction

def process_and_forward(chain, transform_fn):
    def process_fn(tx_data):
        processed = transform_fn(tx_data)
        send_transaction(f'{chain}_processed', processed)
    consume_transactions(chain, process_fn) 