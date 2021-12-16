from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Title, Genre, Category


class TitleResource(resources.ModelResource):

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')


class TitleAdmin(ImportExportModelAdmin):
    resource_class = TitleResource
    list_display = ('pk', 'name', 'year', 'category')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class GenreResource(resources.ModelResource):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug',)


class GenreAdmin(ImportExportModelAdmin):
    resource_class = GenreResource
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('pk', 'name', 'slug',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
