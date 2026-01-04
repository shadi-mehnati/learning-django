from django.urls import path
from . import views


urlpatterns =[
    path('callUs',views.conection),
     path("info/",views.info)
]