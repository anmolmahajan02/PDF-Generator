from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def degree(request):
    return render(request,"degree.html")

def certificate(request):
    return render(request,"certificate.html")

def list(request):
    return render(request,'list.html')

def degreepdf(request):
    return render(request,'degreepdf.html')