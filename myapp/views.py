from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):

    if request.method=='POST':
        check=request.POST['check']
        print(check)

    date = datetime.datetime.now()
    isActive=True
    name="RADHE"
    list_of_programs=[
        'Online Games',
        'Learning New Skills',
        'Devloping Ourself'
    ]
    student={
       'student_name':"ANKIT KUMAR",
        'student_college':"ITR (INSTITUTE OF TECHNOLOGY ROORKEE , ROORKEE)",
        'student_city':'BIHAR'
    }
    print("test function is called")
    #return HttpResponse(f"<h1>Hello Sam, Index page called</h1><p>{date}</p>")
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>This is the About Page</h1>")
    return render(request,"about.html",{})
   
def services(request):
    #return HttpResponse("<h1>This is the Services Page</h1>")
    return render(request,"services.html",{})