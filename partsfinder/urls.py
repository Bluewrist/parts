"""
URL configuration for partsfinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import re_path
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from products.sitemap import PartSitemap, StaticSitemap
from django.contrib.auth import views as auth_views


sitemaps = {
    'product':PartSitemap,
    'static':StaticSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('',include('products.admin_urls')),
    path('api/',include('api.urls')),
    path('',include('crm.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('change-password/',auth_views.PasswordChangeView.as_view(success_url = '/'),name='change_password'),
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]

#handler404 = 'mainapp.views.erro_page'
#handler500 = 'mainapp.views.erro_500'