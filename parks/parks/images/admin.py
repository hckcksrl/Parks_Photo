from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display_links =(
        'location',
    )    

    list_filter = (
        'location',
        'creator'
    )

    list_display = (
        'file',
        'location',
        'creator',
        'create_at',
        'update_at',
    )
