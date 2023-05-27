from rest_framework.viewsets import ModelViewSet
from gameapp.serializers import GameSerializers
from gameapp.models import Game

class GameView(ModelViewSet):

    serializer_class = GameSerializers

    def get_queryset(self):
        return Game.objects.all()
    
