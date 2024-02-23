from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from App.models import*


# Create your views here.
def home(request):
    return render(request,'home.html')
def details(request):
    if request.method == 'POST':
        form = detailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'details.html', {'form': form})