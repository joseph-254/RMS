from django.urls import path
from . import views

urlpatterns =[
    path('', views.signin, name="login"),
    path('signup/', views.signup, name="register"),
    path('signout/', views.signout, name="signout")
]