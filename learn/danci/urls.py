from django.urls import path
from . import views,tests
urlpatterns = [
    path('Index/', views.Index),
    path('VGetWord/', views.GetWord),
    path('TInsert/', tests.TInsert),
    path('TGet/', tests.TGet),
]