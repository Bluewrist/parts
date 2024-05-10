from django.shortcuts import render,redirect
from.models import *
from .filters import PartFilter
from django.contrib import messages
from .forms import PartSearchForm
from django.http import JsonResponse
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.db.models import Q
import datetime
import json






def filtered_parts(request):
    if request.method == 'GET':
        form = PartSearchForm(request.GET)
        if form.is_valid():
            part = form.cleaned_data['part_name']
            model = form.cleaned_data['car_model']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            Equery.objects.create(part_name=part,car_model=model,name=name,last_name=last_name,phone=phone)
            messages.success(request,f"Your enquery has been submited we will contact you soon")
        else:
            msg = 'form is not valid'
    else:
        form = PartSearchForm  
    parts = Part.objects.all()
    cats = Part_category.objects.all()
    f_parts = PartFilter(request.GET,queryset=parts)
    parts = f_parts.qs
    page = request.GET.get('page')
    paginator = Paginator(parts, 2)
    try:
        parts  = paginator.page(page)        
    except PageNotAnInteger:
        parts  = paginator.page(1)
    except EmptyPage:
        parts  = paginator.page(paginator.num_pages)
    context = {'parts':parts,'form':form,'f_parts':f_parts,'cats':cats}
    return context

def cart(request):
    if request.user.is_authenticated:
        user =  request.user.id
        order, created =  Order.objects.get_or_create(customer=user ,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        return redirect('home')

    context =  {'items': items,'order':order,'cartItems':cartItems}
    return render(request, 'front/cart.html',context),


def checkout(request):
    if request.user.is_authenticated:
        user =  request.user.customer
        order, created =  Order.objects.get_or_create(customer=user,complete=False)
        items =  order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        

        context =  {'items': items,'order':order,"dillivery":False,'cartItems':cartItems}
    return render(request, 'front/chackout.html',context)



def updateItem(request):
    data =  json.loads(request.body)
    productId =  data['productId']
    action =  data['action']

    print('Action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Part.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete = False)

    orderitem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderitem.quantity = (orderitem.quantity  + 1)
    elif action == "remove":
        orderitem.quantity = (orderitem.quantity  - 1)
    
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('item was added successfully',safe =  False)


