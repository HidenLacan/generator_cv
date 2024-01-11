from django.db import models

class information(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=300)
    summary = models.TextField(max_length=500)
    school = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    previouswork = models.CharField(max_length=300)
    
    
    

    
