from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Category, Comment, Genre, Review, Title


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


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review
        fields = ('id', 'title', 'text', 'author', 'score',)


class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    list_filter = ['author', 'score']
    search_fields = ('title', 'text')


class CommentResource(resources.ModelResource):

    class Meta:
        model = Comment
        fields = ('id', 'review', 'text', 'author', 'pub_date')


class CommentAdmin(ImportExportModelAdmin):
    resource_class = CommentResource
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')
    list_filter = ['author', 'review']
    search_fields = ('text', )


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
