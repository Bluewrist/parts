from django.shortcuts import render
from.models import *
from .filters import PartFilter
from .forms import ContactForm,PartSearchForm
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.db.models import Q
from .utils import get_client_ip
from datetime import datetime
# Create your views here.
def home(request):
    trending  =  Part.objects.filter(trending = True).order_by('-id')[:8]
    on_sale  = Part.objects.filter(on_sale  = True).order_by('-id')[:8]
    recent  = Part.objects.filter(just_arrived = True ).order_by('-id')[:8]
    context = {
        "trending":trending,
        "on_sale":on_sale,
        "recent":recent,
    }
    return render(request,"front/index.html",context)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        products = Part.objects.filter(Q(part_name__name__icontains=search)|
                                        Q(part_number_1__icontains=search)|
                                        Q(part_number_2__icontains=search)|
                                        Q(part_number_3__icontains=search)
                                        
                                        )
        Search.objects.create(name=search,date=datetime.now(),ip_address=get_client_ip(request))
        
        page = request.GET.get('page')
        paginator = Paginator(products, 20)
        try:
            products  = paginator.page(page)        
        except PageNotAnInteger:
            products  = paginator.page(1)
        except EmptyPage:
            products  = paginator.page(paginator.num_pages)    
        
    return render(request,"front/search.html",{'products':products})

def makes(request):
    mod = Make.objects.all()
    context = {
        'mod':mod
    }
    return render(request,"front/models.html",context)


def watchlist(request):
    return render(request,"front/wishlist.html")
def services(request):
    mod = Manufacture.objects.all()
    context = {
        'mod':mod
    }
    return render(request,"front/service.html",context)


def service_detail(request):
    mod = Manufacture.objects.all()
    context = {
        'mod':mod
    }
    return render(request,"front/service.html",context)

def specialist(request):
    mod = Manufacture.objects.all()
    context = {
        'mod':mod
    }
    return render(request,"front/specilist.html",context)

def specialist_detail(request):
    mod = Manufacture.objects.all()
    context = {
        'mod':mod
    }
    return render(request,"front/service.html",context)


def filtered_parts(request):
    return render(request,'front/parts.html')


def part_detail(request,slug,):
    part = Part.objects.get(slug=slug)
    
    
    context = {'part':part}
    return render(request,'front/part_detail.html',context)


def about(request):
    return render(request,'front/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Thank you for contacting us we will respond as soon as possible ")
        else:
            msg = 'form is not valid'
    else:
        form = ContactForm  
    return render(request, 'front/contact.html',{'form':form })



