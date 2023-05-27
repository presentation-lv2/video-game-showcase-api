from rest_framework import routers
from gameapp.views import GameView

class GameRouter:
    router = routers.SimpleRouter()
    router.register('games', GameView, basename='game')