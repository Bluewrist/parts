import django_filters
from .models import Part
from django_filters import CharFilter,NumberFilter

class PartFilter(django_filters.FilterSet):
    start_price = NumberFilter(field_name="price",lookup_expr='gte',label="Starting Price")
    end_price = NumberFilter(field_name="price",lookup_expr='lte',label="End Price")
   

    class Meta:
        model = Part
        fields = ['car_model']