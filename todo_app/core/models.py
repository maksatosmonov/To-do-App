from django.db import models


class ToDo(models.Model):
    task = models.CharField(max_length=255)
    text = models.TextField()
    priority_choises = [
        ("HIGH", "High"),
        ("MEDIUM", "Medium"),
        ("LOW", "Low"),
    ] 
    priority = models.CharField(max_length=20, choices=priority_choises, default="MEDIUM")
    due_time = models.DateTimeField()
    status_choises = [
        ("DONE", "Done"),
        ("NOT DONE", "Not done"),
    ]
    status = models.CharField(max_length=20, choices=status_choises, default="Not done")

    def __str__(self):
        return self.task
