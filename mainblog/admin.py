from django.contrib import admin

from .models import BlogPost, ThemePost


# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'time_create']
    list_display_links = ['id', 'title']
    list_editable = ['published']
    actions = ['to_publish', 'to_draft']
    search_fields = ['title']

    @admin.action(description='Опубликовать выбранное')
    def to_publish(self, request, queryset):
        count = queryset.update(published=BlogPost.PUBLISHED)
        self.message_user(request, f'Опубликовано: {count}')

    @admin.action(description='Снять с публикации выбранное')
    def to_draft(self, request, queryset):
        count = queryset.update(published=BlogPost.DRAFT)
        self.message_user(request, f'Помещено в черновик: {count}')

    # @admin.display(description='Темы')
    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'theme':
    #         kwargs['queryset'] = ThemePost.objects.all()
    #         return super().formfield_for_manytomany(db_field=db_field, request=request, **kwargs)


@admin.register(ThemePost)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme']
    list_display_links = ['id', 'theme']
