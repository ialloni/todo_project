from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Task
from rest_framework import status
import datetime

from .serializers import TaskSerializer


class TaskAPIView(APIView):

    def get(self, request: Request):
        try:
            user_tg_id = request.query_params['user_tg_id']

        except KeyError:
            return Response({
                'status': 'error',
                'message': 'in query_params dont passed user_tg_id'
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        tasks = Task.objects.all().filter(user_tg_id=user_tg_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    def post(self, request: Request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=KeyError)
        try:
            serializer.save()
        except KeyError:
            return Response({
                'status': 'error',
                'message': 'incorrect data was transmitted'
            },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({'status': 'ok'}, status=status.HTTP_201_CREATED)

class TaskAPIDelPut(APIView):
    def delete(self, request, task_id):
        if not task_id:
            return Response({"error": "Task ID not received"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            del_task = Task.objects.get(id=task_id)
            del_task.delete()
            return Response({"status": "Task deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, task_id):
        put_task = Task.objects.get(id=task_id)
        serializer = TaskSerializer(put_task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskTimeGet(APIView):
    def get(self, request):
        task = Task.objects.all().filter(due_time__range=(datetime.date.today(), datetime.date.today(),))
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
