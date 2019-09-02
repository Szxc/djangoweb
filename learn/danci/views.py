from django.shortcuts import render
from django.http import HttpResponse
from .models import Word, Record
import random


# Create your views here.
def GetWord(request):
    lt1 = Word.objects.order_by('w_ReadNum')
    lt2 = Word.objects.filter(w_ReadNum=lt1[0].w_ReadNum)
    index = random.randint(0, len(lt2)-1)
    wd = lt2[index]
    wd.w_ReadNum += 1
    wd.save()
    return HttpResponse(str(len(lt2))+":"+wd.w_Name + '--' + wd.w_Chinaese + '--' + str(wd.w_ReadNum))
