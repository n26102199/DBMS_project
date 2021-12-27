from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('select_from_where_demo', views.select_from_where_demo, name="select_from_where_demo"),
    path('delete_demo', views.delete_demo, name="delete_demo"),
    path('insert_demo', views.insert_demo, name="insert_demo"),
    path('update_demo', views.update_demo, name="update_demo"),
    path('count_demo', views.count_demo, name="count_demo"),
    path('sum_demo', views.sum_demo, name="sum_demo"),
    path('max_demo', views.max_demo, name="max_demo"),
    path('min_demo', views.min_demo, name="min_demo"),
    path('avg_demo', views.avg_demo, name="avg_demo"),
    path('in_demo', views.in_demo, name="in_demo"),
    path('not_in_demo', views.not_in_demo, name="not_in_demo"),
    path('exists_demo', views.exists_demo, name="exists_demo"),
    path('not_exists_demo', views.not_exists_demo, name="not_exists_demo"),
    path('having_demo', views.having_demo, name="having_demo"),
    ]