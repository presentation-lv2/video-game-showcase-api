from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from gameapp.models import Game, Target, GameTarget

class GameSerializers(ModelSerializer):

    image = CharField()

    class Meta:
        model = Game
        fields = ["id","name","description","realise_date","layout","image"]


class TargetSerializers(ModelSerializer):

    class Meta:
        model = Target
        fields = ["id","name"]

class GameTargetSerializers(ModelSerializer):

    game = GameSerializers(read_only=True)
    target = TargetSerializers(read_only=True)
    game_id = IntegerField(write_only=True)
    target_id = IntegerField(write_only=True)

    class Meta:
        model = GameTarget
        fields = ["id","game","target","game_id","target_id"]