from django.urls import path
from .import views

urlpatterns = [
path('userdata/', views.userData),
path('userregisration/', views.empReg)
]