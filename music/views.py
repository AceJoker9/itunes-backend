from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(primary_key=True)
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


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        serializer = SongSerializer(SongsData, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            song_data = serializer.validated_data
            song_id = len(SongsData) + 1  
            song = (song_id, song_data['title'], song_data['artist'], song_data['album'], song_data['release_date'], song_data['genre'])
            SongsData.append(song)  
            
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['PUT'])
def music_detail(request, pk):
    song = next((song for song in SongsData if song[0] == int(pk)), None)

    if song:
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            song_data = serializer.validated_data
            song = (song[0], song_data.get('title', song[1]), song_data.get('artist', song[2]), song_data.get('album', song[3]), song_data.get('release_date', song[4]), song_data.get('genre', song[5]))
            index = SongsData.index(song)
            SongsData[index] = song

            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response("Song not found", status=404)
    
@api_view(['DELETE'])
def music_detail(request, pk):
    song = next((song for song in SongsData if song[0] == int(pk)), None)

    if song:
        SongsData.remove(song)
        return Response(status=204)
    else:
        return Response("Song not found", status=404)
    




@api_view(['GET'])
def music_detail(request, pk):
    song = next((song for song in SongsData if song[0] == int(pk)), None)

    if song:
        serializer = SongSerializer(song)
        return Response(serializer.data, status=200)
    else:
        return Response("Song not found", status=404)



    




