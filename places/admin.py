from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview', ]
    fields = ['image', 'image_preview', ]


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place',)
    readonly_fields = ['image_preview']
