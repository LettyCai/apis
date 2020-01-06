from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=64,verbose_name=u"标题")
    add_time = models.DateField(auto_now=True,verbose_name=u"添加时间")
    summary = models.CharField(max_length=200,verbose_name=u"摘要")
    click = models.CharField(max_length=64,verbose_name=u"点击数")
    img_url = models.CharField(max_length=300)

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name
        db_table = 'news'