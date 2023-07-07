from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicSerializer
from .models import Music




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
    songs = Music.objects.all()
    serializer = MusicSerializer(songs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



    




