from rest_framework.viewsets import ModelViewSet
from gameapp.serializers import GameSerializers, GameTargetSerializers, TargetSerializers, UsersSerializers, CategorySerialisers, GameCategorySerialisers, PostSerialisers
from gameapp.models import Game, GameTarget, Target, Users, Category, GameCategory, Post
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.filters import SearchFilter

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

    queryset = Game.objects.all()
    serializer_class = GameSerializers
    
class TargetView(ModelViewSet):

    queryset = Target.objects.all()
    serializer_class = TargetSerializers
    
class GameTargetView(ModelViewSet):
    
    serializer_class = GameTargetSerializers 

    def get_queryset(self):
        queryset = GameTarget.objects.all()
        game_id = self.request.GET.get('game_id')
        target_id = self.request.GET.get('target_id')
        if game_id is not None:
            queryset = queryset.filter(game=game_id)
        if target_id is not None:
            queryset = queryset.filter(target=target_id)
        return queryset
               
class UsersView(ModelViewSet):

    serializer_class = UsersSerializers

    def get_queryset(self):
        queryset = Users.objects.all()
        username = self.request.GET.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
    
class CategoryView(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerialisers

class GameCategoryView(ModelViewSet):

    serializer_class = GameCategorySerialisers

    def get_queryset(self):
        queryset = GameCategory.objects.all()
        category = self.request.GET.get('category')
        game = self.request.GET.get('game')
        if category is not None:
            queryset = queryset.filter(category=category)
        if game is not None:
            queryset = queryset.filter(game=game)
        return queryset

class PostView(ModelViewSet):

    serializer_class = PostSerialisers

    def get_queryset(self):
        queryset = Post.objects.all()
        game = self.request.GET.get('game')
        user = self.request.GET.get('user')
        if game is not None:
            queryset = queryset.filter(game=game)
        if category is not None:
            queryset = queryset.filter(user=user)
        return queryset