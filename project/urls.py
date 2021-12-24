from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('select_from_where_demo', views.select_from_where_demo, name="select_from_where_demo"),
    ]