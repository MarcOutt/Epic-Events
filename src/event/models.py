from contract.models import Contract
from customer.models import Customer
from django.db import models
from user.models import CustomUser


class Event(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, limit_choices_to={'role': 'support'},
                                        blank=True, null=True)
    event_ended = models.BooleanField()
    attendees = models.IntegerField()
    event_date = models.DateTimeField(editable=True, blank=True, null=True)
    notes = models.TextField()
