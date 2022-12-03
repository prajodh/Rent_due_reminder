from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name= 'signup'),
    path('login',views.login,name='login'),
    path('generic',views.generic,name='generic'),
    path('tenents',views.tenents,name='tenents')
]