from pydantic import BaseModel, constr
from common.events.types import EventType, ExchangeType


class EventData(BaseModel):
    order_id: str


class ExpirationCompleteEvent(BaseModel):
    event_type: constr(
        regex=f"^{EventType.Expiration.COMPLETE}$") = EventType.Expiration.COMPLETE
    exchange_type: constr(
        regex=f"^{ExchangeType.EXPIRATION}$") = ExchangeType.EXPIRATION
    data: EventData
