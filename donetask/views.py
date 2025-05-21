from django.shortcuts import render
import os 
import json
from django.conf import settings
from .models import Donetask
from django.contrib import messages
# Create your views here.

def index(request):
        done_task=[]
        file_path=os.path.join(settings.BASE_DIR,'jobtask.json')
        with open(file_path,'r') as json_file:
            data=json.load(json_file)
            for k,v in data.items():
                done_task.append({'name':k,'value':v})
        return render(request,'donetask/index.html',{'donetask':done_task})