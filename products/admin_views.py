from django.shortcuts import render
from.models import *
from crm.models import Customer


def admin_home(request):
    return render(request,'dash/index.html')


def all_customers(request):
    customers = Customer.objects.all()
    context = {
        'customers':customers
    }
    return render(request,'dash/customers.html',context)

def customer_detail(request):
    return render(request,'dash/customer_detail.html')


def add_customers(request):
    return render(request,'dash/add_customer.html')

def delete_customer(request):
    return render(request,'dash/customers.html')

def edit_customer(request):
    return render(request,'dash/edit_customer.html')


def all_parts(request):
    parts = Part.objects.all()
    context = {
        'part':parts
    }
    return render(request,'dash/parts.html',context)


def part_detail(request):
    return render(request,'dash/part_detail.html')


def edit_part(request):
    return render(request,'dash/edit_parts.html')


def delete_part(request):
    return render(request,'dash/delete_part.html')


def add_parts(request):
    return render(request,'dash/add_part.html')


def messages(request):
    return render(request,'dash/messages.html')