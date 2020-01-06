from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import News

# Create your views here.
def getNewList(request):
    if request.method == "GET":

        data = News.objects.all()
        print(data)

        return JsonResponse(data,safe=False)