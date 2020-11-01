from pydantic import BaseModel, constr, confloat
from common.events.types import EventType, ExchangeType
from typing import Optional


class TicketData(BaseModel):
    id: str
    price: confloat(gt=0)


class EventData(BaseModel):
    id: str
    user_id: str
    status: constr(
        regex=f"^{EventType.Order.CREATED}$") = EventType.Order.CREATED
    expires_at: str
    ticket: TicketData
    version: Optional[int]


class ExpirationStartCounterEvent(BaseModel):
    event_type: constr(
        regex=f"^{EventType.Expiration.START_COUNTER}$") = EventType.Expiration.START_COUNTER
    exchange_type: constr(
        regex=f"^{ExchangeType.EXPIRATION}$") = ExchangeType.EXPIRATION
    data: EventData
