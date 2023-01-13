from django.db import models

# Create your models here.
class Genre(models.Model):
    genre=models.CharField( max_length=100,null=False)

    def __str__(self):
        return self.genre


class Anime(models.Model):
    ids = models.IntegerField()
    Name=models.CharField(max_length=500, null=True)
    genre=models.ManyToManyField(Genre, blank=True, related_name="genres")
    malRating=models.FloatField(null=True)
    imdbRating=models.FloatField(null=True)
    myRating=models.FloatField(null=True)
    zoro=models.URLField()
    watched=models.BooleanField()
    img=models.URLField(null=True)

    def __str__(self):
        return f"{self.Name}";