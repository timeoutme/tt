from django.shortcuts import render
import json
import urllib.request


# Create your views here.



# 取得问卷数据
# def fetch_survey(url):
#     req = request.Request(url)
#     with request.urlopen(req) as f:
#         data = f.read()
#         return json.loads(data.decode('utf-8'))

url = 'http://www.juoffer.com/api/GetQuestions?key=6eda63c007606b16fe5e558ceb6357d1'
# survey_data = fetch_survey(url)
# survey_data = survey_data['data']

# 提取问卷数据里面的id, title, link, score
def survey_list(request):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as f:
        data = f.read()
    survey_data = json.loads(data.decode('utf-8'))
    survey_data = survey_data['data']
    
    survey_dict = {}
    i = 0
    for survey in survey_data:
        # for key, value in survey.items():
        #     survey_dict = {}
        #     if key == 'id':
                
        #         survey_dict['id'] = value
                
        #     elif key == 'title':
                
        #         survey_dict['title'] = value
                
        #     elif key == 'link':
                
        #         survey_dict['link'] = value
        #     elif key == 'score':
                
        #         survey_dict['score'] = value     
        #         survey_list.append(survey_dict)   
        survey_dict[i] =  survey
        i+=1      
    return render(request,'survey_list.html', {'surveys':survey_dict})   
#     return survey_dict
# a = survey_list(request)    
# print(a)