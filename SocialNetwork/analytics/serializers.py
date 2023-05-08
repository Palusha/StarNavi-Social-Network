from rest_framework import serializers

from posts.models import PostReaction


class PostLikesSerializer(serializers.Serializer):
    post_title = serializers.CharField(max_length=100, read_only=True)
    date = serializers.DateField(read_only=True)
    count = serializers.IntegerField(read_only=True)
