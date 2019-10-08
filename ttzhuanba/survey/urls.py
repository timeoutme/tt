from django.urls import path
from .views import survey_list


urlpatterns = [    
    path('',survey_list,name='问卷列表'),
    
    
]
