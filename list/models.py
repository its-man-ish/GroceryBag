from django.db import models
from customer.models import Profile

from django.urls import reverse
# Create your models here.
ITEM_STATUS = (
        ('BOUGHT', 'BOUGHT'),
        ('NOT-AVAILABLE', 'NOT-AVAILABLE'),
        ('BUY', 'BUY'),
    )
class MyList(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_quantity = models.CharField(max_length=200)
    item_status = models.CharField(max_length=20, choices=ITEM_STATUS)
    created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')

    def get_all_items():
        return MyList.objects.filter()
    
