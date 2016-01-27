from django.contrib import admin

from .models import Image, Question, Choice





class CoverAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['album','artist','image_url']}),
        ('Upload information', {'fields': ['load_date', 'user'], 'classes': ['collapse']}),
    ]
    list_display = ('artist', 'album')
    list_filter = ['album', 'artist','year','load_date']
    search_fields = ['album', 'artist']

admin.site.register(Image, CoverAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['question_text']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)