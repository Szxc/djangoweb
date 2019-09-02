from django.db import models


# Create your models here.
class Word(models.Model):
    w_Name = models.CharField(max_length=30)
    w_Chinaese = models.TextField()
    w_ReadNum = models.IntegerField()


class Record(models.Model):
    r_Name = models.CharField(max_length=30)
    r_InitDT = models.DateTimeField()
    r_DTLen = models.IntegerField()
    r_IsTrue = models.BooleanField()