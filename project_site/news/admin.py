from django.contrib import admin
from .models import News,Category

class NewsAdmin(admin.ModelAdmin):
    list_display=('id','title')

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title')

admin.site.register(News,NewsAdmin)
admin.site.register(Category,CategoryAdmin)

# Register your models here.
