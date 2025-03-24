from django.shortcuts import render
from signapp.models import Signup
from django.http import HttpResponse
# Create your views here.
def signup(request):
    
def login(request):
     
    
def home(request):
    return render(request, 'signup/signup.html')
def login_page(request):
    return render(request, 'signup/login.html')
