from django.db import models


# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=160)
    due = models.DateField()
    completion = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.description.__str__()[:10]
