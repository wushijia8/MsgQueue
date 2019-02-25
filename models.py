# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

from utils.MsgPlugins import get_queue

# Create your models here.


class MsgQueue(models.Model):
    msg = models.CharField(max_length=500, verbose_name=u"队列消息", default=u"", null=True, blank=False)
    queue = models.CharField(max_length=10, verbose_name=u"队列", null=True, blank=True, choices=get_queue())

    class Meta:
        db_table = "msg_queue"
        verbose_name = u"消息内容"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"消息内容"


class Queue(models.Model):
    queue = models.CharField(max_length=10, verbose_name=u"消息队列", default=u"", null=True, blank=False)
    msg = models.CharField(max_length=500, verbose_name=u"消息", default=u"", null=True, blank=False)

    class Meta:
        db_table = "queue"
        verbose_name = u"消息队列"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.queue