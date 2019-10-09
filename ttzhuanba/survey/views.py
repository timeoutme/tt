from django.shortcuts import render
import json
import urllib.request
from django.core.paginator import Paginator

# Create your views here.


url = 'http://www.juoffer.com/api/GetQuestions?key=6eda63c007606b16fe5e558ceb6357d1'

def survey_list(request):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as f:
        data = f.read()
    survey_data = json.loads(data.decode('utf-8'))
    survey_data = survey_data['data']    
    survey_dict = {}
    i = 0
    for survey in survey_data:       
        survey_dict[i] =  survey
        i+=1  

    # 对页面进行分页 
    survey_paginator = Paginator(survey_dict,15)
    page_num = request.GET.get('page',1)
    page_of_surveys = survey_paginator.get_page(page_num) 

    return render(request,'survey_list.html', {'surveys':page_of_surveys})   
