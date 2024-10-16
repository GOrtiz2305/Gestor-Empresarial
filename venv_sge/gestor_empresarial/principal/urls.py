from . import views
from django.urls import path

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('signin/', views.signin, name='signin'),
]