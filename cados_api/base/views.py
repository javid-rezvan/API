from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def endpoins(request):
    data=['/advocates','advocates/:username']
    return JsonResponse(data,safe=False)

def advocate_list(request):
    data=['Dennis','Tadas','Max']
    return JsonResponse(data,safe=False)

def advocate_details(request,username):
    data=username
    return JsonResponse(data,safe=False)