from django.urls import path
from .views import TaskListCreateView, TaskDetailView, BulkTaskCreateView, BulkTaskDeleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/bulk-create/', BulkTaskCreateView.as_view(), name='bulk-task-create'),
    path('tasks/bulk-delete/', BulkTaskDeleteView.as_view(), name='bulk-task-delete'),
]
