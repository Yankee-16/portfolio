from django.conf.urls import url
from django.urls import path
from blog import views

#TEMPLATE TAGGING
app_name = 'blog'

urlpatterns = [
    path('all/', views.all, name='all'),
    path('blogpost/<str:slug>/', views.detail, name='detail'),
    path('post/', views.post, name='post'),
]
