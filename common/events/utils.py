def declare_queue(ch, qs):
    for q in qs:
        ch.queue_declare(q)


def bind_q_to_exchange(ch, qs, exchange):
    for q in qs:
        ch.queue_bind(exchange=exchange, queue=q)
