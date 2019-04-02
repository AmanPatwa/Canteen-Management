from django.urls import path
from . import views


app_name = 'canteen'


urlpatterns = [
    path('', views.index, name="Login"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.gallery, name="gallery"),
    path('redirect/register/', views.register, name="register"),
    path('redirect/', views.redirect, name="redirect"),
    path('login/', views.login, name="login"),
    path('form/', views.food, name="food"),

    # path('redirect/register/', views.signup, name="Signup"),

]
