from django.urls import path
from . import views,tests
urlpatterns = [
    path('GetWord/', views.GetWord),
    path('TInsert/', tests.TInsert),
    path('TGet/', tests.TGet),
]