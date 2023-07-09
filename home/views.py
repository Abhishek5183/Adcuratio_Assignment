from django.shortcuts import render
from home.models import *
from django.http import HttpResponse

# Create your views here.
def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')


def login1(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        idd = Register.objects.filter()
        naa = Register.objects.filter()


    return render(request, 'login1.html')

def register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        na = fn + ln
        mobile = request.POST['mobile']
        email = request.POST['email']
        ps = request.POST['ps']
        cps = request.POST['cps']
        if ps == cps:
            robj = Register.objects.get_or_create(name=na, mob = mobile, em=email, password = ps )[0]
            robj.save()
            return HttpResponse('Succefully registerd')
        else:
            return HttpResponse('Please enter valid Password')
            

    return render(request, 'register.html')

def hotel(request):
    return render(request, 'hotel.html')

