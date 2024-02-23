from django.shortcuts import render,redirect
from App.models import*

def home(request):
    content=student.objects.all()
    data={
        'Data':content
    }
    return render(request,'home.html',data)
def details(request,student_id):
    content= student.objects.get(id=student_id)
    content2=student.objects.filter(id=student_id)
    detail={
        'Detail':content2
    }
    return render(request,'details.html',detail)
