from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from shop.models import Category,Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def allcategories(request):
    c = Category.objects.all()
    return render(request, 'category.html', {'c': c})

@login_required
def allproducts(request,c):
    ct = Category.objects.get(id=c)
    p=Product.objects.filter(category=ct)
    return render(request, 'products.html',{"ct":ct,"p":p})
def userlogin(request):
    if (request.method == 'POST'):
        u = request.POST['user']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return render(request,'category.html')
        else:
            return HttpResponse("no registered user")
    return render(request,'login.html')
def register(request):
    if (request.method == 'POST'):
        u = request.POST['username']
        p = request.POST['password']
        eml = request.POST['email']
        fnm = request.POST['fname']
        lnm = request.POST['lname']

        user = User.objects.create_user(username=u, password=p, email=eml, first_name=fnm, last_name=lnm)
        user.save()
    return render(request,'register.html')
@login_required
def productdtl(request,p):
    km = Product.objects.get(id=p)
    return render (request,"details.html",{'km':km})
@login_required
def user_logout(request):
    logout(request)
    return allcategories(request)
