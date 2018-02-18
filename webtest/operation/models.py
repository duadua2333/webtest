from django.db import models

from txdemo.models import HeroInfo

# Create your models here.


class Comments(models.Model):
    user = models.ForeignKey(HeroInfo, verbose_name=u"文章")
    comments = models.CharField(max_length=150, verbose_name=u"课程")

    class Meta:
        verbose_name = u"游客评论"
        verbose_name_plural = verbose_name
