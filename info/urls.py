from django.conf.urls import url
from info import views

#TEMPLATE TAGGING
app_name = 'info'

urlpatterns = [
    url(r'^education/$', views.education, name='education'),
        
]
