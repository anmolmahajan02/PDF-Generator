from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('degree',views.degree,name="degree"),
    path('certificate',views.certificate,name="certificate"),
    path('list',views.list,name="list"),
    path('degreepdf',views.degreepdf,name="degreepdf"),
]
