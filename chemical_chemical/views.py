from django.shortcuts import render
from django.http import JsonResponse
from .models import Element

# Create your views here.
def element_list(request):
    element_id = request.GET.get('id')
    if element_id:
        elements = Element.objects.filter(id=element_id).values()
    else:
        elements = Element.objects.all().values()
    return JsonResponse(list(elements), safe=False)

def table(request):
    return render(request, 'table.html')