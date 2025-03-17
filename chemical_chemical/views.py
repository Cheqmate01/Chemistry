from django.shortcuts import render
from django.http import JsonResponse
from .models import Element

# Create your views here.
def element_list(request):
    elements = Element.objects.all().values()
    return JsonResponse(list(elements), safe=False)

def table(request):
    return render(request, 'table.html')