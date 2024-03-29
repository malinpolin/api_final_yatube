from django.contrib import admin
from django.conf import settings

from posts.models import Group, Post, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'slug',
    )
    search_fields = ('title', 'slug')
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'author',
        'post',
        'created'
    )
    search_fields = ('text', 'author')
    list_filter = ('created', 'author')
    empty_value_display = settings.EMPTY_VALUE_DISPLAY


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'following',
    )
