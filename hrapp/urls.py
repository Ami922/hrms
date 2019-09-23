from django.urls import path
from .import views

urlpatterns = [
path('projectreg/',views.projectReg),
path('complaintreg/',views.complaintReg)
]