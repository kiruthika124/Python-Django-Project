from django.shortcuts import render
from emapp.models import Employee
# Create your views here.

def emdata(request):
    em_list = Employee.objects.all()
    em_dict = {'em_list': em_list}
    return render(request,"emp.html",context = em_dict)
