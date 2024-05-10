from django.urls import path
from .import admin_views




urlpatterns = [
    path('dashboard',admin_views.admin_home,name='dashboard'),
    path('all_part',admin_views.all_parts,name='all_part'),
    path('detail_part/<int:id>/',admin_views.part_detail,name='detail_part'),
    path('edit_part/<int:id>/',admin_views.edit_part,name='edit_part'),
    path('delete_part/<int:id>/',admin_views.delete_part,name='delete_part'),
    path('all_customers',admin_views.all_customers,name='all_customers'),
    path('detail_customer/<int:id>/',admin_views.customer_detail,name='detail_customers'),
    path('edit_customer/<int:id>/',admin_views.edit_customer,name='edit_customer'),
    path('delete_customer/<int:id>/',admin_views.delete_customer,name='delete_customer'),
    ]
