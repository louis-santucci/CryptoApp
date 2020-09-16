from django.urls import path

from . import views

app_name = 'my_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:user_id>/', views.detail, name='detail'),
    path('create_user/', views.create_user, name='create_user'),
]