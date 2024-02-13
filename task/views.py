from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response({'tasks' :serializer.data})

# Retrieve task by id, update task by id, delete task by id
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class BulkTaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        task_data = request.data.get('tasks', [])

        serializer = self.serializer_class(data=task_data, many=True)
        serializer.is_valid(raise_exception=True)

        tasks = [Task(**item) for item in task_data]
        created_tasks = Task.objects.bulk_create(tasks)

        serializer = self.serializer_class(created_tasks, many=True)
        return Response({'tasks': [{'id': item.id} for item in created_tasks]}, status=status.HTTP_201_CREATED)


class BulkTaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def destroy(self, request, *args, **kwargs):
        task_ids = [task['id'] for task in request.data.get('tasks', [])]
        tasks_to_delete = self.get_queryset().filter(id__in=task_ids)

        if not tasks_to_delete.exists():
            return Response({"error": "No matching tasks found for deletion."}, status=status.HTTP_404_NOT_FOUND)

        tasks_to_delete.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
