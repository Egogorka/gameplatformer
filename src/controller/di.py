from src.view.di import Container

from src.controller.PlayerController import PlayerController
from src.model.Player import Player
from src.view.PlayerView import PlayerView

from src.controller.ViewController import ViewController

Container.set(PlayerController, inModel=Container[Player], inView=Container[PlayerView])
Container.set(ViewController)

Container[ViewController].addView(Container[PlayerView])
