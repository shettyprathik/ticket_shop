from pydantic import BaseModel, constr, confloat
from typing import Optional
from common.events.types import EventType, ExchangeType


class EventData(BaseModel):
    id: str
    price: confloat(gt=0)
    title: constr(min_length=5, max_length=50)
    user_id: str
    order_id: Optional[str]
    version: int


class TicketUpdatedEvent(BaseModel):
    event_type: constr(
        regex=f"^{EventType.Ticket.UPDATED}$") = EventType.Ticket.UPDATED
    exchange_type: constr(
        regex=f"^{ExchangeType.TICKET}$") = ExchangeType.TICKET
    data: EventData
