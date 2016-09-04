from django.db import models
from decimal import Decimal
from datetime import datetime
# Create your models here.
class Expense(models.Model):
    Transaction_No  = models.IntegerField(default =0)
    PaidBy = models.CharField(max_length= 30)
    Amount = models.DecimalField(max_digits=7, decimal_places=2,default = Decimal('0.00'))
    OwnedBy = models.CharField(max_length= 10)
    Description = models.CharField(max_length= 100)
    DateTime = models.DateTimeField(default=datetime.now(), blank=True)
