from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    reviewer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='reviewed_tasks')
    assigned = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='assigned_tasks')
