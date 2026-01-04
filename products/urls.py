from django.urls import path
from . import views



urlpatterns =[
    path('pro', views.production),
    path('pants',views.pants),
    path("shirt",views.shirt)
]