from django.urls import path
from Stocks import views
urlpatterns = [
    path('<str:tid>', views.ticker, name='ticker'),     # subdirectory at ticker level
    path('', views.index, name='index'),
]