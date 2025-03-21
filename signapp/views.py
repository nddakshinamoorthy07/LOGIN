from django.shortcuts import render
from signapp.models import Signup
from django.http import HttpResponse
# Create your views here.
def signup(request):
    get_name = request.POST.get('username')
    get_email = request.POST.get('email')
    get_password = request.POST.get('password')
    get_confirm_password = request.POST.get('confirm_password')
    if get_password == get_confirm_password:
        Signup.objects.create(name=get_name,email=get_email,password=get_password)
        return HttpResponse('Signup Success')
    else:
        return HttpResponse('Password not matched')
def login(request):
    get_email = request.POST.get('email')
    get_password = request.POST.get('password')
    try:
        Signup.objects.get(email=get_email,password=get_password)
        return HttpResponse('Login Success')
    except:
        return HttpResponse('Login Failed')
    
def home(request):
    return render(request, 'signup/signup.html')
def login_page(request):
    return render(request, 'signup/login.html')