from django.forms.widgets import TextInput, Widget
import django_filters 
from django import forms
from .models import MyList
class DateFilter(django_filters.FilterSet):
    created = django_filters.DateFilter()
    created = django_filters.DateFilter(widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    class Meta:
        model = MyList
        fields = ['item_status','created',]

        

        
        
