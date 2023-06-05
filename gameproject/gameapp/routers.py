from rest_framework import routers
from gameapp.views import GameView, TargetView, GameTargetView, UsersView, CategoryView, GameCategoryView

class GameRouter:
    router = routers.SimpleRouter()
    router.register('games', GameView, basename='game')

class TargetRouter:
    router = routers.SimpleRouter()
    router.register('target', TargetView, basename='target')

class GameTargetRouter:
    router = routers.SimpleRouter()
    router.register('gametargets', GameTargetView, basename='game-target')

class UsersRouter:
    router = routers.SimpleRouter()
    router.register('users', UsersView, basename='users')

class CategoryRouter:
    router = routers.SimpleRouter()
    router.register('category', CategoryView, basename='category' )

class GameCategoryRouter:
    router = routers.SimpleRouter()
    router.register('gameCategory', GameCategoryView, basename='game-category' )

class PostRouter:
    router = routers.SimpleRouter()
    router.register('post', PostView, basename='post')