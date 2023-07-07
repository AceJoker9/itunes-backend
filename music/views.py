from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


class SongSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()  # Set id field as read-only
    title = serializers.CharField()
    artist = serializers.CharField()
    album = serializers.CharField()
    release_date = serializers.CharField()
    genre = serializers.CharField()





SongsData = [
    (1, "Billie Jean", "Michael Jackson", "Thriller", "1982", "R&B"),
    (2, "Purple Rain", "Prince", "Purple Rain", "1984", "R&B"),
    (3, "Super Freak", "Rick James", "Street Songs", "1981", "R&B"),
    (4, "I Wanna Dance with Somebody", "Whitney Houston", "I'm your baby tonight", "1981", "R&B"),
    (5, "Rock with You", "Michael Jackson", "Off The Wall", "1979", "R&B"),
    (6, "Sweet Child o' Mine", "Guns N' Roses", "Appetite for Destruction", "1987", "R&B"),
]


@api_view(['GET'])
def music_list(request):
    serializer = SongSerializer(SongsData, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, pk):
    song = next((song for song in SongsData if song[0] == int(pk)), None)

    if song:
        serializer = SongSerializer(song)
        return Response(serializer.data, status=200)
    else:
        return Response("Song not found", status=404)


