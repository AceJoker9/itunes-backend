from rest_framework.decorators import api_view
from rest_framework.response import Response
from datamusic import SongList

# Create your views here.
@api_view(['GET'])
def music_list(request):

    return Response('ok')