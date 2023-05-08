from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, PostReaction
from .serializers import PostSerializer


class PostViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
        Creates new post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def react_to_post(self, request, pk=None, reaction='like'):
        user = request.user

        post = Post.objects.get(pk=pk)
        PostReaction.objects.update_or_create(post=post, user=user, defaults={'reaction': reaction})

    @action(detail=True, methods=['post'], url_path='like', name='Like post')
    def like_post(self, request, pk=None):
        self.react_to_post(request, pk)
        return Response({'message': 'You liked the post'})

    @action(detail=True, methods=['post'], url_path='unlike', name='Unlike post')
    def dislike_post(self, request, pk=None):
        self.react_to_post(request, pk, reaction='dislike')
        return Response({'message': 'You disliked the post'})
