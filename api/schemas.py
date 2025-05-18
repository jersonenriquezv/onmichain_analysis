from pydantic import BaseModel
from typing import List, Optional, Any

class TokenTransfer(BaseModel):
    token: str = 'UNKNOWN'
    amount: int = 0
    from_address: Optional[str] = None
    to_address: Optional[str] = None

class TransactionSchema(BaseModel):
    hash: str
    chain: str
    sender: str
    receiver: Optional[str]
    fee: int
    token_transfers: List[Any] = []

class GasFeeTrendResponse(BaseModel):
    window: str
    average_fee: float

class TokenMovementResponse(BaseModel):
    token: str
    volume: int

class ArbitrageOpportunity(BaseModel):
    description: str
    details: Any 