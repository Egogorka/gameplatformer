import pygame


from src.utility.EventListener import EventListener


class ViewController(EventListener):


    def __init__(self ):
        self._views = []
        self._display = pygame.display.set_mode([600, 600], pygame.HWSURFACE | pygame.DOUBLEBUF)

    def on_init(self):
        for view in self._views:
            view.on_init()

    def eventFired(self, event):
        if( event.type == "on_render" ):
            for view in self._views:
                render = view.on_render()
                self._display.blit(render["surface"], render["position"])
            pygame.display.flip()


    def addView(self, view):
        self._views.append(view)
