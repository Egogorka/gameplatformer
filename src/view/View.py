from abc import ABCMeta, abstractmethod


class View( metaclass= ABCMeta):


    @abstractmethod
    def on_render(self):
        pass

    @abstractmethod
    def on_init(self):
        pass