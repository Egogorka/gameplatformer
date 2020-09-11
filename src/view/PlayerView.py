import pygame

from src.view.View import View
from src.model.Player import Player


states = 4
imgProps = {
    "width": 100,
    "height": 40,

    "stateWidth": 25,
}


class PlayerView:


    def __init__(self, inModel : Player):
        self._player = inModel

        self._cState = 0

    def on_init(self):
        self._img = pygame.image.load("images/sprites/player.png").convert()

    def on_render(self):
        return {
            "surface" : self.drawPlayer(self._cState),
            "position" : self.getPosition(),
        }


    def drawPlayer(self, state):
        canvas = pygame.Surface((imgProps["stateWidth"], imgProps["height"]))
        canvas.blit(self._img, [0, 0], area=pygame.Rect((imgProps["stateWidth"]*state,0),(imgProps["stateWidth"], imgProps["height"])))
        return canvas


    def getPosition(self):
        return self._player.pos

