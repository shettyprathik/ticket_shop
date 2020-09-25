from pydantic import BaseModel, constr, confloat
from common.events.types import EventType, ExchangeType


class EventData(BaseModel):
    id: str
    price: confloat(gt=0)
    title: constr(min_length=5, max_length=50)
    user_id: str


class TicketCreatedEvent(BaseModel):
    event_type: constr(
        regex=EventType.Ticket.CREATED) = EventType.Ticket.CREATED
    exchange_type: constr(regex=ExchangeType.TICKET) = ExchangeType.TICKET
    data: EventData
