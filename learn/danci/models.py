from django.db import models


# Create your models here.
class Word(models.Model):
    w_Name = models.CharField(max_length=30)
    w_Chinaese = models.TextField()
    w_ReadNum = models.IntegerField()

    def __str__(self):
        return {"w_Name": self.w_Name,
                "w_Chinaese": self.w_Chinaese,
                "w_ReadNum": self.w_ReadNum
                }


class Record(models.Model):
    r_Name = models.CharField(max_length=30)
    r_InitDT = models.DateTimeField()
    r_DTLen = models.IntegerField()
    r_IsTrue = models.BooleanField()
