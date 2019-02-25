from django.http import QueryDict
from django.http.response import HttpResponse
import redis
import json

from rest_framework.views import APIView

# Create your views here.


class MsgQueueAPI(APIView):
    def post(self, request):
        msgObject = {}
        conn = redis.StrictRedis()
        keys = conn.keys()
        for x in keys:
            msgObject[x] = conn.zrange(x, 0, -1)
        return HttpResponse('{"status":"success","res":' + json.dumps(msgObject, ensure_ascii=False) + '}',
                            content_type="application/json")

    def delete(self, request):
        key = request.data[u"key"]
        queue = request.data[u"queue"]
        conn = redis.StrictRedis()
        res = conn.zrem(queue, key)
        return HttpResponse('{"status":"success","res":' + json.dumps(res, ensure_ascii=False) + '}',
                            content_type="application/json")


class QueueAPI(APIView):
    def post(self, request):
        conn = redis.StrictRedis()
        keys = conn.keys()
        return HttpResponse('{"status":"success","res":' + json.dumps(keys) + '}', content_type="application/json")

    def delete(self, request):
        key = request.data[u"key"]
        conn = redis.StrictRedis()
        res = conn.delete(key)
        return HttpResponse('{"status":"success","res":' + json.dumps(res) + '}', content_type="application/json")
