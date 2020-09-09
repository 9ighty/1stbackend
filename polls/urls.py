from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('infor', views.infor),
    path('home',views.home_),  # view_function
    path('form', views.createform), # ชื่อ path ชื่อ file
    path('addform', views.addusers),
    path('loginform',views.loginform),
    path('login', views.login)
]