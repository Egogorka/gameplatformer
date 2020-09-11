from src.utility.Eventer import Eventer
from src.utility.EventListener import EventListener


class Player(Eventer, EventListener):


    def __init__(self, x, y):
        super(Player, self).__init__()
        self._x = x
        self._y = y

        self._vx = 0
        self._vy = 0

        self._ax = 0
        self._ay = 0

        self._counter = 0

    def move(self, v):
        self._x += v
        self.fireEvent("move")

    def jump(self, y):
        self._y += y
        self.fireEvent("jump")

    def accelerate(self):
        self._ax = 1

    def update(self):
        self._x += self._vx
        self._vx += self._ax

        self._x += self._vy
        self._vy += self._ay

    def eventFired(self, event):
        if( event == "on_loop"):
            self.update()
            

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def pos(self):
        return (self._x, self._y)