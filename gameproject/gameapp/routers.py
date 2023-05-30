from rest_framework import routers
from gameapp.views import GameView, TargetView, GameTargetView

class GameRouter:
    router = routers.SimpleRouter()
    router.register('games', GameView, basename='game')

class TargetRouter:
    router = routers.SimpleRouter()
    router.register('target', TargetView, basename='target')

class GameTargetRouter:
    router = routers.SimpleRouter()
    router.register('gametargets', GameTargetView, basename='game-target')