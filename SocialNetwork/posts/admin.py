from django.contrib import admin

from .models import Post, PostReaction


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'created_at')
    list_display_links = ('id', 'title', 'content', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__username', 'created_at')


class PostReactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'reaction', 'last_modified')
    list_display_links = ('id', 'post', 'user', 'reaction', 'last_modified')
    list_filter = ('last_modified',)
    search_fields = ('post__title', 'user__username', 'last_modified')


admin.site.register(Post, PostAdmin)
admin.site.register(PostReaction, PostReactionAdmin)
