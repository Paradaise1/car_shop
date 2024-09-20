from django.contrib import admin

from .models import Car, Comment


admin.site.empty_value_display = 'Не задано'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin's model for comments.'''
    list_display = ('content', 'created_at')
    list_editable = ('content',)
    list_display_links = ('created_at',)


@admin.register(Car)
class PostAdmin(admin.ModelAdmin):
    '''Admin's model for cars.'''
    list_display = (
        'make',
        'model',
        'year',
        'description',
        'created_at',
        'updated_at',
        'owner',
    )
    list_editable = ('year', 'description',)
    search_fields = ('make', 'model',)
    list_filter = ('make', 'model',)
    list_display_links = ('make', 'model',)
