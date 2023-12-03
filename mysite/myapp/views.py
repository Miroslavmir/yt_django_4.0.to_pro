from django.shortcuts import render
from django.http import HttpResponse
from .models import Product



def index(request):
    items = Product.objects.all()
    context = {
        'items': items
    }
    # return HttpResponse(items)
    return render(request, 'myapp/index.html', context)



def indexItem(request, my_id):
    # return HttpResponse('Your item id is:" + str(my_id)')
    item = Product.objects.get(id=my_id)
    contex = {
        'item': item
    }
    return render(request, 'myapp/detail.html', context=contex)

#


