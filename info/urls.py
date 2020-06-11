from django.conf.urls import url
from info import views

#TEMPLATE TAGGING
app_name = 'info'

urlpatterns = [
    url(r'^education/$', views.education, name='education'),
    url(r'^job/$', views.job, name='job'),
    url(r'^extracurricular/$', views.extracurricular, name='extracurricular'),
    url(r'^photos/$', views.photogal, name='photos'),
    url(r'^contact/$', views.contact, name='contact'),
]
