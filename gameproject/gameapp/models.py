from django.db import models

class Game(models.Model):

    id = models.IntegerField(primary_key=True,null=False)
    name = models.CharField(null=False, max_length= 200)
    description = models.CharField(null=False)
    realise_date = models.DateField(null=False)
    image = models.BinaryField()

    def __str__(self):
        return self.name
    

