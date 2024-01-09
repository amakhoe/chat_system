from django.urls import path, include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.roomses, name="room" ),
    path('<slug:slug>/', views.room, name="room" ),

]
