




@api_view(['GET'])
def music_detail(request, pk):
    song = next((song for song in SongsData if song[0] == int(pk)), None)

    if song:
        serializer = SongSerializer(song)
        return Response(serializer.data, status=200)
    else:
        return Response("Song not found", status=404)