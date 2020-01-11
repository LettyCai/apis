from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import News,NewsDetail
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
                     "url":"http://127.0.0.1:8000/"+new.img.url
                     })

    result = {"status": 0}
    result["message"]=list

    return HttpResponse(json.dumps(result), content_type="application/json")

class getNewView(View):
    def get(self,request,id):
        print(id)

        #news_detail = list(NewsDetail.objects.filter(id=id))

        result = {"status": 0}
        #result["message"] = news_detail

        return HttpResponse(json.dumps(result), content_type="application/json")




