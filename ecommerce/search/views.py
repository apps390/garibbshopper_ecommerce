from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product,Category
from django.db.models import Q

# Create your views here.
def search(request):
    if request.method == "POST":
        query = request.POST['srch']
        prdt=Product.objects.filter( Q(name__contains=query) | Q(category__name__contains=query))
        if(prdt):
            cnt=Product.objects.filter(Q(name__contains=query) | Q(category__name__contains=query)).count()
            return render(request, 'search.html', {'query': query,'prdt':prdt,'cnt':cnt})
        else:
            return HttpResponse('no result')

    return render(request, 'search.html',)
