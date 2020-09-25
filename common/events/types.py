from enum import Enum


class EventType:
    class Ticket(Enum):
        CREATED = 'TICKET_CREATED'
        UPDATED = 'TICKET_UPDATED'
