from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import News
import json

# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,"index.html")


def getNewslist(request):

    list = []
    newslist = News.objects.all()
    for new in newslist:
        list.append({"title":new.title,
                     "time":str(new.add_time),
                     "click":new.click,
                     "url":new.img_url})

    result = {"status": 0}
    result["message"]=list

    return HttpResponse(json.dumps(result), content_type="application/json")




