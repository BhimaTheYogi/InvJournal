from django.db import models

# Create your models here.
class Journal(models.Model):
    journal_user_id = models.ForeignKey('UserProfil.User', default=None, on_delete=models.CASCADE)
    ticker_symbole = models.CharField(max_length=10)
    qty = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    
    possition_choices = [ 
                 ('LONG', 'Long'),
                 ('SHORT', 'Short'),
                 ('CALL', 'Call'),
                 ('PUT', 'Put'),
                 ]
                                    #LONG = 'Long'
                                    #SHORT = 'Short'
                                    #CALL = 'Call'
                                    #PUT = 'Put'
                                    #STOCK = 'Stock'
                                    #OPTION = 'Option'
                                    #FUTURES = 'Futures'
    possition = models.CharField(max_length=10, choices=possition_choices)
    possition_choices = [ 
                 ('LONG', 'Long'),
                 ('SHORT', 'Short'),
                 ('CALL', 'Call'),
                 ('PUT', 'Put'),
                 ]
    type_trade_options = [ 
            ('STOCK', 'Stock'),
            ('OPTION', 'Option'),
            ('FUTURES', 'Futures'),
            ]
    type_trade = models.CharField(max_length=10, choices=type_trade_options)
    Open_date = models.DateField(max_length=20)
    close_date = models.DateField(max_length=20)
    journal = models.TextField(max_length=20)
    creation_date = models.DateField(auto_now_add=True)
    
    def is_upperclass(self):
        return self.possition
    
    def __int__(self):
        return self.id