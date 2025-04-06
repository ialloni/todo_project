import datetime
import time

from rest_framework import serializers
from .models import Task
from utils.hash_id import hash_id


class TaskSerializer(serializers.ModelSerializer):
    due_time = serializers.DateField()
    class Meta:
        model = Task
        fields = ('content', 'category', 'user_tg_id', 'created_at', 'due_time')

    def create(self, validated_data: dict) -> Task:
        task_id = hash_id(validated_data.get('user_tg_id'), time.time())
        due_time_dt = validated_data.pop('due_time')
        return Task.objects.create(**validated_data, id=task_id, due_time=due_time_dt)

    def update(self, instance: Task, validated_data: dict) -> Task:
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.due_time = validated_data.get('due_time', instance.due_time)
        instance.save()
        return instance
