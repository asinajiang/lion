from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # 引用django自带的用户模型

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_time = models.DateTimeField(default=timezone.now())
    # created_time = models.DateTimeField(auto_now_add=True)  效果同上一行
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)
    read_num = models.IntegerField(default=0)
