from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('counter/', views.counter, name='counter'),
    path('counter/', views.Counter.as_view(), name='counter')
]
