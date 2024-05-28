from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', index),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('news/search/', news_search, name='news_search'),
    path('news/create', news_create, name='create'),
    path('403/', error_403, name='error_403'),
    path('news/<int:pk>/edit/', edit_news, name='edit_news'),
    path('news/<int:pk>/delete/', delete_news, name='delete_news'),
    path('articles/create/', create_category, name='create_category'),


    path('yandex-login/', yandex_login, name='yandex_login'),

]

