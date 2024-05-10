from django.contrib.sitemaps import Sitemap
from .models import Part
from django.urls import reverse
 
 
class PartSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Part.objects.all()
        
    def location(self,obj):
        return '/part-detail/%s' % (obj.slug)




class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home','contact']

    def location(self, item):
        return reverse(item)
