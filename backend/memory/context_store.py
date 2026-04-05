class ContextStore:
    def __init__(self):
        self.history = []

    def add(self, entry):
        self.history.append(entry)

    def get_recent(self, n=3):
        return self.history[-n:]


# global instance
context_store = ContextStore()
