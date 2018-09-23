from django.db import models
from django.contrib.auth.model

class post (models.Models):
    get_name= models.CharField(max_length=100)
    user = models.ForeignKey(user)
     
