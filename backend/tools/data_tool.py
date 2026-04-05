from memory.context_store import context_store

def store_context(data):
    context_store.add(data)


def get_context():
    return context_store.get_recent()
