from django.contrib import admin

# Register your models here.
from .models import News,NewsDetail

class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News,NewsAdmin)

class NewsDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(NewsDetail,NewsDetailAdmin)