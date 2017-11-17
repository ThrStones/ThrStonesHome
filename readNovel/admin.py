from django.contrib import admin

# Register your models here.
from readNovel.models import NovelInfo, Chapter

admin.site.register(NovelInfo)
admin.site.register(Chapter)
