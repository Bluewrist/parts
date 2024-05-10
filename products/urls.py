from django.urls import path
from .import views




urlpatterns = [
    path('',views.home,name='home'),
    path('all_parts',views.filtered_parts,name='all_parts'),
    path('part-detail/<str:slug>',views.part_detail,name='part-detail'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search'),
    path('models',views.makes,name='models'),
    path('services',views.services,name='services'),
    path('service_detail/<int:id>/',views.service_detail,name='service_detail'),
    path('specialist',views.specialist,name='specilists'),
    path('specialist_detail/<int:id>/',views.specialist_detail,name='specialis_detail'),
    path('services',views.services,name='services'),
    path('watchlist',views.watchlist,name='watchlist'),
  
    ]
