from django.db import models

# Create your models here.
class Lyric(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)


class LyricLine(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    timestamp = models.FloatField()
