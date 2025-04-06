from django.contrib import admin
from django.urls import path

from tasks.views import TaskAPIView, TaskTimeGet, TaskAPIDelPut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/task/', TaskAPIView.as_view()),
    path('api/v1/taskdel/<str:task_id>', TaskAPIDelPut.as_view()),
    path('api/v2/task/', TaskTimeGet.as_view())
]
