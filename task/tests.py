from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'is_completed': False}
        self.task = Task.objects.create(**self.task_data)
        self.task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        self.task_list_url = reverse('task-list-create')
        self.bulk_create_url = reverse('bulk-task-create')
        self.bulk_delete_url = reverse('bulk-task-delete')

    def test_create_task(self):
        response = self.client.post(self.task_list_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_retrieve_task(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'is_completed': True}
        response = self.client.put(self.task_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertEqual(self.task.is_completed, updated_data['is_completed'])

    def test_delete_task(self):
        response = self.client.delete(self.task_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_bulk_create_tasks(self):
        tasks_data = [{'title': 'Task 1', 'is_completed': False}, {'title': 'Task 2', 'is_completed': True}]
        data = {'tasks': tasks_data}
        response = self.client.post(self.bulk_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)

    def test_bulk_delete_tasks(self):
        task_to_delete = Task.objects.create(title='Task to Delete', is_completed=False)
        task_ids = [self.task.id, task_to_delete.id]
        data = {'tasks': [{'id': task_id} for task_id in task_ids]}
        response = self.client.delete(self.bulk_delete_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id__in=task_ids).exists())
