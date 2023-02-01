from django.urls import path
from .views import TaskView, TaskCreate,apiOverview,TaskDetail,TaskUpdate,TaskDelete

from .views import TaskDetail
from . import views

urlpatterns = [	
	path('',apiOverview, name="api-overview"),
	path('task-list/', TaskView.as_view(), name="task-list"),
	path('task-detail/<str:pk>/', TaskDetail.as_view(), name="task-detail"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
	path('task-update/<str:pk>/', TaskUpdate.as_view(), name="task-update"),
	path('task-delete/<str:pk>/', TaskDelete.as_view(), name="task-delete"),
]
