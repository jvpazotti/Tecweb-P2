from django.db import models

# Create your models here.

from django.db import models

# class Tag(models.Model):

#     name = models.CharField(max_length=200,null=True)

#     def __str__(self):
#         return str(self.name)


# class Note(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     content=models.TextField(null=True)

#     def __str__(self):
#         return f"{self.id}.{self.title}"


# class Artist(models.Model):
    
#     name = models.CharField(max_length=200)

#     def  __str__(self):

#         return str(self.name)

class Song(models.Model):

    song_id = models.IntegerField()

    def __str__(self):
        return f"{self.id}.{self.song_id}"


