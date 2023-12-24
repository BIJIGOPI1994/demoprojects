from django.shortcuts import render,redirect
from shop.models import category,product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def allcategories(request):
    a=category.objects.all()
    return render(request,'category.html',{'allcat':a})


def allproducts(request,p):
    c=category.objects.get(name=p)
    pro=product.objects.filter(category=c)
    return render(request,'product.html',{'c':c,'p':pro})

def details(request,p):
    pro=product.objects.get(name=p)
    return render(request,'detail.html',{'p':pro})


def register(request):
    if(request.method=="POST"):
        u=request.POST["u"]
        p=request.POST["p"]
        cp=request.POST["cp"]
        e=request.POST["e"]
       
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            return redirect("shop:allcat")
        else:
            return redirect("password not matching")
    return render(request,'regi.html')

def user_login(request):
    if(request.method=="POST"):
        name=request.POST['u']
        pass1=request.POST['p']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            messages.error(request,"Invalid credentails")
    return render(request,'login.html')

def user_logout(request):
    logout(request)  
    return redirect('shop:allcat')
