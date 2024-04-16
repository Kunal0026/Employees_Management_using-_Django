from django.http import HttpResponse
from django.shortcuts import render
import datetime

from django.shortcuts import render

def home(request):

    isActive = True
    if request.method=='POST':
        check = request.POST.get('check')
        print(check)
        if check is None : isActive = False
        else : isActive =True

    date = datetime.datetime.now()
    name = "Patil Kunal Sapana Pravin"
    list_of_friends = [
        'Mahesh',
        'Akshay',
        'Ajinkya',
        'Vikas',
        'Jayesh'
    ]
    friend = {
        'friend_name' : "Mahesh Patil",
        'friend_add' : "Ankleshwr",
        'friend_job' : "QA"
    }

    data={
        'date' : date,
        'isActive' : isActive,
        'name' : name,
        'list_of_friends' : list_of_friends,
        'friend_data' : friend

    }
    return render(request,"home.html",data)


def about(request):
    # html = "<h1>  my self is patil </h1>"
    # return HttpResponse (html)
    return render(request,"about.html",{})

def services(request):
    # html = "<h1> this is my services </h1>"
    # return HttpResponse (html)
    return render(request,"services.html",{})