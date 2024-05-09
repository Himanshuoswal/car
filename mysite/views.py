from django.http import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def Home(request):
    return render (request, "index.html")



def carvaluation(request):
    return render(request,"carvaluation.html")




def emicalculator(request):
    return render (request , "emicalc.html")



def challan(request):
    return render (request , "challan.html")


def blog(request):
    return render(request , "blog.html")



def delhi(request):
    return render(request , "delhi.html")


def mumbai(request):
    return render(request , "mumbai.html")


def banglore(request):
    return render(request , "banglore.html")


def ahemdabad(request):
    return render(request , "ahemdabad.html")


def surat(request):
    return render(request , "surat.html")



def loan(request):
    return render(request , "loan.html")





@login_required(login_url='login')


def HomePage(request):
  return render(request,'loginhome.html')

def SignupPage(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1')
       pass2=request.POST.get('password2')
       if pass1!= pass2:
          return HttpResponse('your password and conform password is not same')
       else:
          my_user=User.objects.create_user(uname,email,pass1)
          my_user.save()
          return redirect('login')

    return render(request,'signup.html')


def LoginPage(request):
   if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('password')
       user =authenticate(request,username=username,password=pass1)
       if user is not None:
          login(request,user )
          return redirect('home')
       else:
            return HttpResponse('Username or password is incorrect')
      
   return render(request,'login.html')


def LogoutPage(request):
   logout(request)
   return redirect('login')
       