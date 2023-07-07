from rest_framework import serializers

class SongSerializer(serializers.Serializer):
    title = serializers.CharField()
    artist = serializers.CharField()
    album = serializers.CharField()
    release_date = serializers.CharField()
    genre = serializers.CharField()
