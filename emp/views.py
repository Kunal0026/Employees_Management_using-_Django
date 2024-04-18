from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp

# Create your views here.
def emp_home(request):

    emps = Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps' : emps
    })


def add_emp(request):
    if request.method =="POST":
        # print("data is coming")

        # data fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_work = request.POST.get("emp_work")
        emp_dept = request.POST.get("emp_dept")

        # validation

        # create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept
        if emp_work is None:
            e.working = False
        else:
            e.working = True

        # save the object
        e.save()

        # prepare msg


        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

    
def do_update_emp(request,emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_work = request.POST.get("emp_work")
        emp_dept = request.POST.get("emp_dept") 

        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_dept
        if emp_work is None:
            e.working = False
        else:
            e.working = True
        
        e.save()

    return redirect("/emp/home/")