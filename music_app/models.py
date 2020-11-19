from django.db import models

# Create your models here.


class PlayList(models.Model):
    objects = models.Manager()
    name_list = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.name_list


class Song(models.Model):
    objects = models.Manager()
    img_song = models.ImageField(upload_to='image/',blank=True)
    song_file = models.FileField(upload_to='mp3/',blank=True)
    name_song = models.CharField(default='', max_length=255)
    auth = models.CharField(default='', max_length=255)
    play_list = models.ForeignKey(PlayList, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name_song





