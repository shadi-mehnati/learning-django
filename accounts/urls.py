from django.urls import path
from . import views

urlpatterns=[
    path("userlist/", views.userlist),
    path('profile/<str:username>',views.profile),
   
]
