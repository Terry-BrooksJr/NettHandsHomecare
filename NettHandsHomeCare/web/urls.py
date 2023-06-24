from django.urls import path
import web.views

urlpatterns = [
    path("", views.index, name='index'),
    
]