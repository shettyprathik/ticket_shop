class ExchangeType:
    TICKET = 'TICKET'
    ORDER = 'ORDER'


class EventType:
    class Ticket:
        CREATED = 'TICKET_CREATED'
        UPDATED = 'TICKET_UPDATED'

    class Order:
        CREATED = 'ORDER_CREATED'
        CANCELLED = 'ORDER_CANCELLED'
        AWAIT_PAYMENT = 'ORDER_AWAIT_PAYMENT'
        COMPLETE = 'ORDER_COMPLETE'


def get_events(event_type_obj):
    return [getattr(event_type_obj, attr) for attr in dir(event_type_obj) if not callable(
        getattr(event_type_obj, attr)) and not attr.startswith("__")]
