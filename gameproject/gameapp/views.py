from rest_framework.viewsets import ModelViewSet
from gameapp.serializers import GameSerializers, GameTargetSerializers, TargetSerializers, UsersSerializers
from gameapp.models import Game, GameTarget, Target, Users
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

class SwaggerView:
    schema_view = get_schema_view(
        openapi.Info(
            title="Game showcase API",
            default_version="v1",
            description="API for game showcase app"
        ),
        public= True
    )

class GameView(ModelViewSet):

    serializer_class = GameSerializers

    def get_queryset(self):
        return Game.objects.all()
    
class TargetView(ModelViewSet):

    serializer_class = TargetSerializers

    def get_queryset(self):
        return Target.objects.all()
    
class GameTargetView(ModelViewSet):

    serializer_class = GameTargetSerializers

    def get_queryset(self):
        return GameTarget.objects.all()
    
class UsersView(ModelViewSet):

    serializer_class = UsersSerializers

    def get_queryset(self):
        return Users.objects.all()
    