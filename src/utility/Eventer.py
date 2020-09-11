from src.utility.EventListener import EventListener

class Eventer:

    def __init__(self):
        self._observers = []

    def addListener(self, inObserver : EventListener):
        self._observers.append(inObserver)

    def removeListener(self, inObserver : EventListener):
        self._observers.remove(inObserver)

    def fireEvent(self, event):
        for x in self._observers:
            x.eventFired(event)