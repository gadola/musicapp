from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.MusicView.as_view(),name='index')
]
