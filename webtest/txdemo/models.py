from django.db import models


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_data = models.DateField()

    def __unicode__(self):
        return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    gender = models.BooleanField(default=True)
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

# 注册表单相关模型类


class UserMessage(models.Model):
    object_id = models.CharField(max_length=5, primary_key=True, default="", verbose_name=u"主键")
    name = models.CharField(max_length=10, verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=20, verbose_name=u"联系地址")
    message = models.CharField(max_length=50, verbose_name=u"简介")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
