from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=64,verbose_name=u"标题")
    add_time = models.DateField(auto_now=True,verbose_name=u"添加时间")
    summary = models.CharField(max_length=200,verbose_name=u"摘要")
    click = models.CharField(max_length=64,verbose_name=u"点击数")
    img_url = models.CharField(max_length=300)
    img = models.ImageField(max_length=1000,upload_to='static/images/', verbose_name=u'图片', null=True, blank=True)

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name
        db_table = 'news'

class NewsDetail(models.Model):
    title = models.CharField(max_length=64, verbose_name=u"标题")
    add_time = models.DateField(auto_now=True, verbose_name=u"添加时间")
    click = models.CharField(max_length=64, verbose_name=u"点击数")
    content = models.CharField(max_length=2000, verbose_name=u"详细内容")

    class Meta:
        verbose_name = u'新闻详情'
        verbose_name_plural = verbose_name
        db_table = 'newsdetail'