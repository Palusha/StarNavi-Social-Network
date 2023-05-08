from rest_framework import serializers

from .models import Post, PostReaction


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ('pk', 'user', 'reaction')


class PostSerializer(serializers.ModelSerializer):
    post_reactions = ReactionSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content', 'author', 'created_at', 'post_reactions')
        read_only_fields = ('author', 'created_at')

    def create(self, validated_data):
        request = self.context.get('request')
        
        if request.user is not None and request.user.is_authenticated:
            validated_data['author'] = request.user
        return super().create(validated_data)
