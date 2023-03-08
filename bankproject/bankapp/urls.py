from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('button',views.button,name='button'),
    path('bankapp/form', views.person_create_view, name='form'),

]