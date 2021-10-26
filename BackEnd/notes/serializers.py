from rest_framework import serializers
from .models import Artist, Note, Song


# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = ['id', 'title', 'content']


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:

        model = Artist
        fields=['id','name']

class SongSerializer(serializers.ModelSerializer):

    class Meta:

        model = Song
        fields=['id','artist','name']


