from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Product
from cart.models import Cart,Order,Account


# Create your views here.
@login_required
def viewcart(request):
    u = request.user
    c = Cart.objects.filter(user=u)
    total=0
    for i in c:
        total=total+(i.quantity*i.product.price)

    return render(request, 'cart.html', {'c': c,'total':total})


@login_required
def addtocart(request, p):
    p = Product.objects.get(id=p)
    u = request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        if p.stock > 0:
            c.quantity += 1
            p.stock -= 1
            p.save()
            c.save()
    except:
        if p.stock > 0:
            c = Cart.objects.create(user=u, product=p, quantity=1)
            p.stock -= 1
            p.save()
            c.save()
    return viewcart(request)


def remove_quantity(request, k):
    p = Product.objects.get(id=k)
    u = request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        if c.quantity > 1:
            c.quantity -= 1
            p.stock += 1
            p.save()
            c.save()
        else:
            c.delete()
            p.stock+=1
            p.save()

    except:
        pass

    return viewcart(request)


def remove_item(request, r):
    p = Product.objects.get(id=r)
    u = request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        p.stock += c.quantity
        print(p.stock)
        p.save()
        c.delete()
    except:
        pass
    return viewcart(request)
def placeorder(request):
    if request.method=="POST":
        a=request.POST['adrs']
        p=request.POST['phn']
        acc=request.POST['acno']
        u = request.user
        c = Cart.objects.filter(user=u)
        print(c)
        total = 0
        for i in c:
            total = total + (i.quantity * i.product.price)
        try:
            acc=Account.objects.get(account_no=acc)
            if(acc.amount>=total):
                acc.amount=acc.amount-total
                acc.save()
                for i in c:
                    od=Order.objects.create(user=u,product=i.product,no_of_items=i.quantity, address=a,phone=p,order_status='paid')
                    od.save()
                    print('success')
                c.delete()
                msg='order placed successfully'
                return render(request,'orderdetails.html',{'msg':msg})
            else:
                msg = 'Insufficient Balance'
                return render(request, 'orderdetails.html', {'msg': msg})
        except:
            pass

    return render(request,'order.html')