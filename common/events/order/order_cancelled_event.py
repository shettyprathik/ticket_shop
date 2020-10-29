from pydantic import BaseModel, constr, confloat
from common.events.types import EventType, ExchangeType


class TicketData(BaseModel):
    id: str


class EventData(BaseModel):
    id: str
    ticket: TicketData
    version: int


class OrderCancelledEvent(BaseModel):
    event_type: constr(
        regex=f"^{EventType.Order.CANCELLED}$") = EventType.Order.CANCELLED
    exchange_type: constr(regex=f"^{ExchangeType.ORDER}$") = ExchangeType.ORDER
    data: EventData
