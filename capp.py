import pygame
from pygame.locals import *

import cevent
from src.utility.Eventer import Eventer
from src.utility.Event import Event

from src.controller.di import Container

# change CApp into
class CApp(cevent.CEvent, Eventer):

    def __init__(self):
        cevent.CEvent.__init__(self)
        Eventer.__init__(self)
        self._running = True

    def on_init(self):
        pygame.init()
        self._running = True    #inner variable, currently manages the loop


    def on_loop(self):
        self.fireEvent(Event("on_loop", None))

    def on_render(self):
        self.fireEvent(Event("on_render", None))

    def on_cleanup(self):
        print("Goodbye")
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.fireEvent(Event("event", event))
                self.on_event(event)
            self.on_render()
            self.on_loop()
        self.on_cleanup()


Container.set(CApp)

if __name__ == "__main__":
    theApp = CApp()
    theApp.on_execute()