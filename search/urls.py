from django.urls import path

from . import views


urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
    path('load-testing/', views.LoadTestSearchView.as_view(), name='search_load_testing')
]
