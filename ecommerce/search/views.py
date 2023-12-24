from django.shortcuts import render
from shop.models import product
from django.db.models import Q

def search(request):
    q = ""
    p=None
    if(request.method=="POST"):
        q = request.POST['q']
        if q:
            p=product.objects.filter(Q(name__icontains=q)|Q(id__icontains=q))
    return render(request, 'search.html', {'p':p,'query':q})