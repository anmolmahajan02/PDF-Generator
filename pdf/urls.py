from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('degree',views.degree,name="degree"),
    path('cv',views.cv,name="cv"),
    path('degreepdf',views.degreepdf,name="degreepdf"),
    path('cvpdf',views.cvpdf,name="cvpdf"),
]
