from django.urls import path
from .views import element_list, table

urlpatterns = [
    path('', table, name='table'),
    path('api/elements/', element_list, name='element_list'),
]
