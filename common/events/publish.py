import json


def publish_event(channel, event_info):
    event_info = event_info.dict()
    channel.basic_publish(
        exchange=event_info['exchange_type'], routing_key=event_info['event_type'], body=json.dumps(event_info['data']))
