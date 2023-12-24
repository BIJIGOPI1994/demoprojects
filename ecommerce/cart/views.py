from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import product
from cart.models import cart
from cart.models import Account,Order

# Create your views here.
def cartview(request):
    total=0
    u=request.user
    try:
        c=cart.objects.filter(user=u)

        for i in c:
            total+=i.quantity*i.product.price
    except:
        pass
      
    return render(request,'cart.html',{'c':c,'total':total})

@login_required
def add_to_cart(request,p):
    pro=product.objects.get(name=p)
    u=request.user
    try:
        c=cart.objects.get(user=u,product=pro)
        if(c.quantity<c.product.stock):
            c.quantity+=1
        c.save()
    except:    
        c=cart.objects.create(product=pro,user=u,quantity=1)
        c.save()
        
        
    return redirect('cart:cartview')

def cart_remove(request,p):
    pro=product.objects.get(name=p)
    user=request.user
    try:
        c=cart.objects.get(user=user,product=pro)
        if c.quantity>1:
            c.quantity-=1
            c.save()
        else:
            c.delete()      
            
    except:
        pass
    return redirect('cart:cartview')


def full_remove(request,p):
    pro=product.objects.get(name=p)
    user=request.user
    try:
        c=cart.objects.get(user=user,product=pro)
        
        c.delete()      
            
    except:
        pass
    return redirect('cart:cartview')

def orderform(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        u=request.user
        c=cart.objects.filter(user=u)
    
    #total amount calculate
        total=0
        for i in c:
            total+=i.quantity*i.product.price
    
        ac=Account.objects.get(acctnum=n)#amount minus in database code  
        if(ac.amount>=total):
            ac.amount=ac.amount-total
            ac.save()
            
            
            for i in c:  #creates record in Order table for each object in cart table for the current user
                o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                o.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            c.delete()  #clears the cart items for the current user
            msg="Order placed Successfully"
            return render(request,'orderdetails.html',{'m':msg})
        else:
            msg="Insufficient Amount in User Account.You cannot place order."  
            return render(request,'orderdetails.html',{'m':msg})
    return render(request,'orderform.html')
        
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o})
