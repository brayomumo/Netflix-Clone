from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movies$',views.index, name= "index"),
    url(r'',views.homepage,name='home'),
]
