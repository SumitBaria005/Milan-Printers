from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Milan Printers', 'name': 'Sumit'})
