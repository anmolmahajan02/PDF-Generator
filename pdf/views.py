from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.template.loader import render_to_string
from django.http import HttpResponse
import pdfkit
import os

config = pdfkit.configuration(wkhtmltopdf=os.path.join('C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')) 

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

def cv(request):
    if request.method == "POST":
        name = request.POST.get('name') 
        uniName = request.POST.get('uniName') 
        degreeName = request.POST.get('degree') 
        cgpa = request.POST.get('cgpa')
        achievements = request.POST.get('achievements')

        query_string = urlencode({
            'name': name,
            'uniName': uniName,
            'degree': degreeName,
            'cgpa': cgpa,
            'achievements':achievements,})
        cv_url = reverse('cvpdf')
        return redirect(f"{cv_url}?{query_string}")
    else:
        return render(request,"cv.html")

def list(request):
    return render(request,'list.html')

def degreepdf(request):
    context = {
        'name' : request.GET.get('name') ,
        'uniName' : request.GET.get('uniName') ,
        'degreeName' : request.GET.get('degree') ,
        'cgpa' : request.GET.get('cgpa')
    }
    
    html = render_to_string('degreepdf.html',context)

    options = {
        'page-size':'A4',
        'orientation':'Landscape'
    }
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'inline; filename ="degree.pdf"'
    return response

def cvpdf(request):
    name = request.GET.get('name')
    uniName = request.GET.get('uniName')
    degreeName = request.GET.get('degree')
    cgpa = request.GET.get('cgpa')
    achievements = request.GET.get('achievements')
    achievement = achievements.split(',')

    context = {
        'name' : name ,
        'uniName' : uniName ,
        'degreeName' : degreeName ,
        'cgpa' : cgpa,
        'achievements':achievement
    }
    return render(request,"cvpdf.html",context)
