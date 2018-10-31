from django.urls import path

from .views import *

urlpatterns = [
    # Users
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),

    # Tasks
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateAPIView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),

    path('tasks/assigned-to/<int:user_id>/', AssignedTasksAPIView.as_view(), name='assigned-task-list'),
]
