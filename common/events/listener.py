def listen(channel, event_info, callback):
    event_info = event_info.dict()
    channel.basic_consume(queue=event_info['event_type'],
                          on_message_callback=callback)
