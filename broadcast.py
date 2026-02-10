class BroadcastManager:
    def __init__(self):
        # map
        self.listeners = {}

    def on_message(self, message_name, callback):
        # registeration
        if message_name not in self.listeners:
            self.listeners[message_name] = []
        self.listeners[message_name].append(callback)

    def broadcast(self, message_name, data=None):
        # send it
        if message_name in self.listeners:
            for callback in self.listeners[message_name]:
                if type(data) != None:
                    callback(data)
                else:
                    callback()

emitter = BroadcastManager()