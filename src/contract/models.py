from customer.models import Customer
from django.db import models
from user.models import CustomUser


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, limit_choices_to={'role': 'sale'})
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField(editable=True)

    def __str__(self):
        return str(self.id)