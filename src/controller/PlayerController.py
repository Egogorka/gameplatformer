import pygame
import pygame.locals

from src.utility.Eventer import Eventer
from src.utility.EventListener import EventListener
from src.utility.Event import Event

from src.model.Player import Player
from src.view.PlayerView import PlayerView


class PlayerController(EventListener): #Observes app events

    def __init__(self, inModel : Player, inView : PlayerView ):
        self._player = inModel
        self._view = inView

    def eventFired(self, event : Event):
        if( event.type == "event"):
            if( event.state.type == pygame.locals.KEYDOWN):
                if  ( event.state.key == pygame.K_RIGHT):
                    self._player.move(5)
                elif( event.state.key == pygame.K_LEFT):
                    self._player.move(-5)
                elif( event.state.key == pygame.K_UP):
                    self._player.jump(5)
                elif( event.state.key == pygame.K_DOWN):
                    self._player.jump(-5)

