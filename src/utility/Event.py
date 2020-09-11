
class Event:


    def __init__(self, type, state):
        self._type = type
        self._state = state

    @property
    def type(self):
        return self._type

    @property
    def state(self):
        return self._state