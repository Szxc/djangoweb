from django.test import TestCase
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from .models import Word, Record


# 数据库操作
def TInsert(request):
    test1 = Word(w_Name='runoob', w_Chinaese='菜鸟', w_ReadNum=0)
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def TGet(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Word.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Word.objects.filter(w_ReadNum=500)

    # 获取单个对象
    response3 = Word.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    response4=Word.objects.order_by('w_ReadNum')

    # 数据排序
    Word.objects.order_by("id")

    # 上面的方法可以连锁使用
    Word.objects.filter(w_Name="runoob").order_by("id")

    # 输出所有数据
    for var in response4:
        response1 += str(var.w_Name) + "|"
    response = response1
    return HttpResponse("<p>" + response + "</p>")
