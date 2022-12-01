from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
def sr1(request):
    queryset=Children.objects.select_related('fparentf').all()
    return render(request,'page1.html',{'x':list(queryset)})

def sr2(request):
    queryset='ddd'
    return HttpResponse(f'{queryset}')



