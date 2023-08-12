from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"forms.html")

def postdata(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        context={
            "name":name
        }
        return render(request,"output.html",context)
