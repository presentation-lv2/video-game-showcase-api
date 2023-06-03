from rest_framework.serializers import ModelSerializer, CharField, IntegerField, FileField, SerializerMethodField, StringRelatedField
from gameapp.models import Game, Target, GameTarget, Users, Category, GameCategory
from django.conf import settings

class GameSerializers(ModelSerializer):

    image = FileField(write_only=True)
    image_url = SerializerMethodField()

    def get_image_url(self, obj):
        req = self.context.get('request')
        if obj.image:
            return req.build_absolute_uri(obj.image.url)
        return None

    class Meta:
        model = Game
        fields = ["id","name","description","realise_date","layout","image","image_url"]


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

class UsersSerializers(ModelSerializer):

    class Meta:
        model = Users
        fields = ["id","username","password","role"]

class CategorySerialisers(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]

class GameCategorySerialisers(ModelSerializer):
    
    game = GameSerializers(read_only=True)
    game_id = IntegerField(write_only=True)
    category = CategorySerialisers(read_only= True)
    category_id = IntegerField(write_only=True)
    class Meta:
        model = GameCategory
        fields = ["id", "game", "game_id", "category", "category_id"]