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
#     tag=models.ForeignKey(to=Tag ,on_delete=models.SET_NULL,null=True)

#     def __str__(self):
#         return f"{self.id}.{self.title}"


class Artist(models.Model):
    
    name = models.CharField(max_length=200)

    def  __str__(self):

        return str(self.name)

class Song(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.artist},{self.name}"


