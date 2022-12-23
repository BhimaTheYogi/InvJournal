from django.db import models



# Create your models here.
class User(models.Model): 
    user_first_name = models.CharField(max_length=20)
    user_last_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=100)   
    user_user_name = models.CharField(max_length=20)
    user_join_date = models.DateField(auto_now_add=True)
    #social media

    
    def __int__(self):
        return self.id
    