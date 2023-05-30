from django.db import models

class Game(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(null=False, max_length= 200)
    description = models.CharField(null=False)
    realise_date = models.DateField(null=False)
    layout = models.CharField()
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
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Users(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    username = models.CharField(null=False)
    role = models.CharField(null=False)

    def __str__(self):
        return self.username

class Post(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    message = models.CharField(null=False)
    game = models.ForeignKey(Game, related_name='game_id', on_delete=models.CASCADE)
    poster = models.ForeignKey(Users, related_name='poster', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.message


class Target(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(null=False)

    def __str__(self):
        return self.name


class GameTarget(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    game = models.ForeignKey(Game, related_name='game', on_delete=models.CASCADE)
    target = models.ForeignKey(Target, related_name='target', on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    