from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$',views.index),
    url(r'^(?P<id>\d+)/buy$',views.buy),
    url(r'^reciept$',views.reciept),
    url(r'^checkout$',views.reset)
]