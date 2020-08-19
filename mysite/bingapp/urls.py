'''urls file of bingapp
'''
from django.conf.urls import url
from bingapp import views

urlpatterns = [
    url(r'^search/', views.search, name='bing search'),
    url(r'^list/', views.search_list, name='list of search results'),
    url(r'^detail/', views.get_details, name='details of search results'),
]
