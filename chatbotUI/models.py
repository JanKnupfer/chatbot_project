from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=180)

    # id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.task
