from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View
from .models import News
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,"index.html")

class GetNewsListView(View):
    def get(self,request):

        temp_output = serializers.serialize('python', News.objects.all(),ensure_ascii=False)
        temp_output = json.dumps(temp_output,ensure_ascii=False,cls=DjangoJSONEncoder)

        print(temp_output)

        return HttpResponse(temp_output, content_type="application/json")




