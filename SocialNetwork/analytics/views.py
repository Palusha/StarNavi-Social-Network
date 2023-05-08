from django.db.models.functions import TruncDate
from django.db.models import Count, F
from rest_framework import generics

from posts.models import PostReaction
from .serializers import PostLikesSerializer


class LikeCountView(generics.ListAPIView):
    serializer_class = PostLikesSerializer

    def get_queryset(self):
        queryset = PostReaction.objects.select_related('post')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if date_from is not None and date_to is not None:
            queryset = queryset.filter(last_modified__date__range=(date_from, date_to))
        elif date_from is not None:
            queryset = queryset.filter(last_modified__gte=date_from)
        elif date_to is not None:
            queryset = queryset.filter(last_modified__lte=date_to)

        queryset = queryset.annotate(
            date=TruncDate('last_modified'), post_title=F('post__title')
            ).values('post_title', 'date').annotate(count=Count('id')).order_by('date', 'post_title')

        return queryset
