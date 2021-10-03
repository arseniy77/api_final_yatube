from django.contrib import admin

from .models import Comment, Follow, Group, Post

BLANK_VALUE_CONST = '-пусто-'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = BLANK_VALUE_CONST


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'post')
    search_fields = ('text',)
    list_filter = ('author',)
    empty_value_display = BLANK_VALUE_CONST


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user',)
    list_filter = ('following',)
    empty_value_display = BLANK_VALUE_CONST


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title',)
    list_filter = ('description',)
    empty_value_display = BLANK_VALUE_CONST
