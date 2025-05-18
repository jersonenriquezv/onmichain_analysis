import os
from snowflake.connector import connect
from dotenv import load_dotenv

load_dotenv()

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')

# This is a stub. In production, use parameterized queries and handle connections properly.
def insert_transaction_snowflake(tx):
    ctx = connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    cs = ctx.cursor()
    try:
        cs.execute("""
            INSERT INTO transactions (hash, chain, sender, receiver, fee, token_transfers)
            VALUES (%(hash)s, %(chain)s, %(sender)s, %(receiver)s, %(fee)s, %(token_transfers)s)
        """, tx)
    finally:
        cs.close()
        ctx.close() 