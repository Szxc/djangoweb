from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Word, Record
from django.db.models import Sum
import random
import datetime


# Create your views here.
def Index(request):
    return render(request, 'index.html', dict())


name = ''
dt = datetime.datetime.now()
wd = Word()


def GetWord(request):
    global name, dt, wd
    result = []
    sd = request.GET.get('sd')
    if name == sd or (name != sd and name):
        rd = Record()
        rd.r_Name = name
        rd.r_InitDT = datetime.datetime.now()
        rd.r_DTLen = (datetime.datetime.now() - dt).seconds
        rd.r_IsTrue = name == sd
        rd.save()

    if not name or name == sd:
        lt1 = Word.objects.order_by('w_ReadNum')
        lt2 = Word.objects.filter(w_ReadNum=lt1[0].w_ReadNum)
        index = random.randint(0, len(lt2) - 1)
        wd = lt2[index]
        wd.w_ReadNum += 1
        wd.save()
        name = wd.w_Name
        result.append(name)
    elif name != sd:
        result.append(wd.w_Name)
        result.append(wd.w_Chinaese)

    rd1 = Record.objects.filter(r_Name=name)
    rd2 = Record.objects.filter(r_Name=name, r_IsTrue=0)
    rd3 = Record.objects.filter(r_Name=name, r_IsTrue=1)
    info = '查看:{0}</br>时长:{1}</br>记忆:{2}</br>True:{4}</br>False:{3}'.format(wd.w_ReadNum - 1, rd1.aggregate(Sum("r_DTLen"))['r_DTLen__sum'],len(rd1),len(rd2),len(rd3))
    result.append(info)
    dt = datetime.datetime.now()
    return JsonResponse({'data': result})
