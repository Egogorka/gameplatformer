from abc import ABCMeta, abstractmethod

class EventListener(metaclass = ABCMeta):
    """
    Абстрактный суперкласс для всех наблюдателей.
    """
    @abstractmethod
    def eventFired(self, event):
        """
        Метод который будет вызван у наблюдателя при изменении модели.
        """
        pass

    # @property
    # @abstractmethod
    # def observables(self):
    #     """
    #     Массив названий эвентов, которые будет наблюдать наблюдатель
    #     """
    #     pass


# class EventListener():
#     _listeners = []
#     def __init__(self):
#         self._listeners.append(self)
#         self._observables = {}
#     def observe(self, event_name, callback):
#         self._observables[event_name] = callback
#
#

# class Event():
#     def __init__(self, name, data, autofire = True):
#         self.name = name
#         self.data = data
#         if autofire:
#             self.fire()
#     def fire(self):
#         for listener in EventListener._listeners:
#             if self.name in listener._observables:
#                 listener._observables[self.name](self.data)