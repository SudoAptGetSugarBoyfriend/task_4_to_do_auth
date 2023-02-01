from base.models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


class TaskView(APIView):

    def get(self, request, format=None):
        snippets = Task.objects.all().order_by('id')
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)


class TaskDetail(APIView):

    def get(self, request, *args, **kwargs):
        snippet = self.kwargs.get('pk')
        tasks = Task.objects.get(id=snippet)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)


class TaskCreate(APIView):

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUpdate(APIView):

    def put(self, request, *args, **kwargs):
        snippet = self.kwargs.get('pk')
        task_ins = Task.objects.get(id=snippet)
        serializer = TaskSerializer(instance=task_ins, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class TaskDelete(APIView):

    def delete(self, request, *args, **kwargs):
        snippet = self.kwargs.get('pk')
        task_ins = Task.objects.get(id=snippet)
        task_ins.delete()
        return Response("item successfully deleted")




