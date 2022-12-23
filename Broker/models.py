from django.db import models
from UserProfil.models import User

# Create your models here.
class Broker(models.Model):
    broker_user_id = models.ForeignKey('UserProfil.User', default=None, on_delete=models.CASCADE)
    broker_name = models.CharField(max_length=20)
    broker_user_name = models.CharField(max_length=20)
    broker_password = models.CharField(max_length=20)
    broker_account_date = models.CharField(max_length=20)
    broker_account_number = models.CharField(max_length=20)
    broker_starting_balance = models.CharField(max_length=20)
    broker_profit_loss = models.CharField(max_length=20)
    
    def __int__(self):
        return self.id