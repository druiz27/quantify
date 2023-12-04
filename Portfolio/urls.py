from django.urls import path
from Portfolio import views

urlpatterns = [
    path('', views.investment_interface, name='investment_interface')
]