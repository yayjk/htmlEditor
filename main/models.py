from django.db import models
from datetime import datetime

# Create your models here.


class codeDb(models.Model):
    the_code = models.TextField()
    time_of_execution = models.CharField(max_length=200, blank=False)
    count = models.PositiveSmallIntegerField()
