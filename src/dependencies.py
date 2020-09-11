from src.controller.PlayerController import PlayerController
from src.controller.ViewController import ViewController

from src.model.Player import Player


from capp import Container, CApp


app = Container[CApp]

app.addListener(Container[PlayerController])
app.addListener(Container[ViewController])
app.addListener(Container[Player])

Container[ViewController].on_init()