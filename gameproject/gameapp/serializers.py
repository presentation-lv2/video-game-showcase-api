from rest_framework.serializers import ModelSerializer, CharField
from gameapp.models import Game

class GameSerializers(ModelSerializer):

    image = CharField()

    class Meta:
        model = Game
        fields = ["id","name","description","realise_date","layout","image"]