from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_url'),
    path('create/', views.new_post, name='new_post_url'),
]
                                     
