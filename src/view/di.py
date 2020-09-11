from src.model.di import Container

from src.model.Player import Player
from src.view.PlayerView import PlayerView

Container.set(PlayerView, inModel=Container[Player])




