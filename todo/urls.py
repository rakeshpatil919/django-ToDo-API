from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('', views.taskOverview, name="task-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
    path('api-token-auth/', auth_view.obtain_auth_token, name='api-token-auth'),
    path('logout/', views.logout, name='logout')
  ]