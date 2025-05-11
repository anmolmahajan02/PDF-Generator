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
        #Basic Info
        name = request.POST.get('name') 
        uniName = request.POST.get('uniName') 
        degreeName = request.POST.get('degree')
        branch = request.POST.get('branch')
        #Education
        shortDegree = request.POST.get('shortDegree')
        collegeBatch = request.POST.get('collegeBatch')
        cgpa = request.POST.get('cgpa')
        seniorSecondary = request.POST.get('seniorSecondary')
        seniorSecondaryMarks = request.POST.get('seniorSecondaryMarks')
        seniorSecondaryBatch = request.POST.get('seniorSecondaryBatch')
        secondary = request.POST.get('secondary')
        secondaryMarks = request.POST.get('secondaryMarks')
        secondaryBatch = request.POST.get('secondaryBatch')
        
        #
        skills = request.POST.get('skills')
        #
        #personal Details
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        linkedin = request.POST.get('linkedin')
        github = request.POST.get('github')

        query_string = urlencode({
            #Basic Info
            'name': name,
            'uniName': uniName,
            'degree': degreeName,
            'branch': branch,
            #Education
            'shortDegree':shortDegree,
            'collegeBatch':collegeBatch,
            'cgpa': cgpa,
            'seniorSecondary':seniorSecondary,
            'seniorSecondaryMarks':seniorSecondaryMarks,
            'seniorSecondaryBatch':seniorSecondaryBatch,
            'secondary':secondary,
            'secondaryMarks':secondaryMarks,
            'secondaryBatch':secondaryBatch,
            'skills':skills,
            #personal details
            'phone':phone,
            'email':email,
            'linkedin':linkedin,
            'github':github,
            })
        cv_url = reverse('cvpdf')
        return redirect(f"{cv_url}?{query_string}")
    else:
        return render(request,"cv.html")



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
    branch = request.GET.get('branch')
    #Education
    shortDegree = request.GET.get('shortDegree')
    collegeBatch = request.GET.get('collegeBatch')
    cgpa = request.GET.get('cgpa')
    seniorSecondary = request.GET.get('seniorSecondary')
    seniorSecondaryMarks = request.GET.get('seniorSecondaryMarks')
    seniorSecondaryBatch = request.GET.get('seniorSecondaryBatch')
    secondary = request.GET.get('secondary')
    secondaryMarks = request.GET.get('secondaryMarks')
    secondaryBatch = request.GET.get('secondaryBatch')
    #personal details
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    linkedin = request.GET.get('linkedin')
    github = request.GET.get('github')
        
        #
    skills = request.GET.get('skills')
        #
    skill = []
    if skills:
        skills_list = skills.split(",")
        for i in skills_list:
            s=i.strip().capitalize
            skill.append(s)
    

    context = {
        #Basic Info
        'name': name,
        'uniName': uniName,
        'degree': degreeName,
        'branch': branch,
        #Education
        'shortDegree':shortDegree,
        'collegeBatch':collegeBatch,
        'cgpa': cgpa,
        'seniorSecondary':seniorSecondary,
        'seniorSecondaryMarks':seniorSecondaryMarks,
        'seniorSecondaryBatch':seniorSecondaryBatch,
        'secondary':secondary,
        'secondaryMarks':secondaryMarks,
        'secondaryBatch':secondaryBatch,
        'skills':skill,
        #personal details
        'phone':phone,
        'email':email,
        'linkedin':linkedin,
        'github':github,
    }
    html = render_to_string('cvpdf.html',context)

    options = {
        'page-size':'A4',
        'orientation':'Portrait'
    }
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type = 'application/pdf')
    response['Content-Disposition'] = 'inline; filename ="cv.pdf"'
    return response
