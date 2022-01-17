from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Examples(models.Model):
    examples = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.task





