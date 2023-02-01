from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, RegisterPage

urlpatterns = [
    path('accounts/register/', RegisterPage.as_view(), name='register'),
    path('', TaskListView.as_view(), name='todo'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
