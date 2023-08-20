from django.urls import path
from . import views

urlpatterns = [
    path('schedule/', views.meetdeet, name='schedule'),
    path('', views.home, name='home'),
    path('sectionA/', views.sectionA, name='sectionA'),
    path('sectionB/', views.sectionB, name='sectionB'),
    path('sectionC/', views.sectionC, name='sectionC'),
]
