from src.dependencies import Container
from capp import CApp


app = Container[CApp]

app.on_init()
app.on_execute()
