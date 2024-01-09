from django.urls import path, include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('', views.front, name="frontpage" ),
    path('registro/', views.registro, name="registro"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login")
]
