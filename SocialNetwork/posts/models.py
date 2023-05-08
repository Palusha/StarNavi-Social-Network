from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class PostReaction(models.Model):
    REACTION_STATUSES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    post = models.ForeignKey(Post, related_name='post_reactions', on_delete=models.CASCADE, verbose_name='Post')
    user = models.ForeignKey(get_user_model(), related_name='post_reactions', on_delete=models.CASCADE, verbose_name='User')
    reaction = models.CharField(max_length=20, choices=REACTION_STATUSES, default='like', verbose_name='Reaction')
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'PostReaction'
        verbose_name_plural = 'PostReactions'

    def __str__(self):
        return f'{self.user} - {self.post} reaction: {self.reaction}'
