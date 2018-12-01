from django.contrib import admin
from .models import Article

# Register your models here.
# 可以定制后台文章管理列表第一行表头显示


# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 表示表头显示id,author,title和created_time等
    list_display = ("id", "author", "is_deleted", "title", "read_num", "created_time", "last_updated_time")
    ordering = ("id", )  # 表示后台文章按照id正序排列，若设置为ordering = ("-id", )或者不设置则为倒序排列


admin.site.register(Article, ArticleAdmin)  # 等效与上面第8行
