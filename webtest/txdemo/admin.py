from django.contrib import admin
from txdemo.models import *


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_data']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'message']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(UserMessage, UserMessageAdmin)