from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    return render(request,'index.html')

def degree(request):
    if request.method == "POST":
        name = request.POST.get('name') 
        uniName = request.POST.get('uniName') 
        degreeName = request.POST.get('degree') 
        cgpa = request.POST.get('cgpa') 

        query_string = urlencode({
            'name':name,
            'uniName':uniName,
            'degree':degreeName,
            'cgpa':cgpa})
        degreepdf_url = reverse('degreepdf')
        return redirect(f"{degreepdf_url}?{query_string}")
    else:
        return render(request,"degree.html")

def certificate(request):
    return render(request,"certificate.html")

def list(request):
    return render(request,'list.html')

def degreepdf(request):
    name = request.GET.get('name') 
    uniName = request.GET.get('uniName') 
    degreeName = request.GET.get('degree') 
    cgpa = request.GET.get('cgpa')
    
    return render(request, "degreepdf.html", {
        'name': name,
        'uniName': uniName,
        'degree': degreeName,
        'cgpa': cgpa
    })