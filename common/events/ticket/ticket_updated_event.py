from pydantic import BaseModel, constr, confloat
from common.events.types import EventType, ExchangeType


class TicketUpdatedEvent(BaseModel):
    event_type: constr(
        regex=EventType.Ticket.UPDATED) = EventType.Ticket.UPDATED
    exchange_type: constr(regex=ExchangeType.TICKET) = ExchangeType.TICKET
    data: str
