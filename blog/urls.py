from django.urls import path
from . import views
urlpatterns = [
    path('', views.showform),
    path('searched/', views.post_list),
]