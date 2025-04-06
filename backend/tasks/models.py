from django.db import models


class Task(models.Model):
    id = models.CharField(primary_key=True)
    content = models.TextField()
    user_tg_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_time = models.DateField(null=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.content
