# _*_ encoding:utf-8 _*_
"""
@Time:2019-02-22 16:28:27
@Author:jaris
"""
from django.contrib import messages
import time
import xadmin
from xadmin.views import ListAdminView

from .models import *
from utils.MsgPlugins import *


class MsgQueueAdmin(object):
    msg = True
    list_display = ['msg']
    search_fields = []
    list_filter = []
    list_export = ()
    list_exclude = ['id']
    show_bookmarks = False

    def save_models(self):
        msg = self.new_obj.msg
        queue = self.new_obj.queue
        if queue is None:
            messages.error(self.request, "消息 \"" + msg + "\" 添加失败，当前未选择队列")
            messages.set_level(self.request, messages.ERROR)
        else:
            conn = redis.StrictRedis()
            conn.zadd(queue, time.time(), msg)


class QueueAdmin(object):
    queue = True
    list_display = ['queue']
    search_fields = []
    list_filter = []
    list_export = ()
    list_exclude = ['id']
    show_bookmarks = False

    def save_models(self):
        queue = self.new_obj.queue
        msg = self.new_obj.msg
        conn = redis.StrictRedis()
        conn.zadd(queue, time.time(), msg)


xadmin.site.register(MsgQueue, MsgQueueAdmin)
xadmin.site.register(Queue, QueueAdmin)
xadmin.site.register_plugin(MsgQueuePlugin, ListAdminView)
xadmin.site.register_plugin(QueuePlugin, ListAdminView)
