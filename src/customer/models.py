from django.db import models
from user.models import CustomUser


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'sale'},
                                      related_name='customer')

    def __str__(self):
        return self.company_name
