from django.contrib import admin
from .models import Word,Comment
# Register your models here.


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'partOfSpeech')
    list_filter = ('name',)
    ordering = ('name',)
    search_fields = ("name",)
    list_per_page = 5


admin.site.register(Word, WordAdmin)
admin.site.register(Comment)


