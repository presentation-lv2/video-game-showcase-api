from django.db import models

class Game(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(null=False, max_length= 200)
    description = models.CharField(null=False)
    realise_date = models.DateField(null=False)
    image = models.BinaryField()

    def __str__(self):
        return self.name
    
class Category(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(null=False, max_length = 200)

    def __str__(self):
        return self.name


class GameCategory(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    game = models.ForeignKey(Game, related_name='game_fk', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_fk', on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name