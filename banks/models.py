from django.db import models

# Create your models here.
class bank(models.Model):
    id = models.BigIntegerField(primary_key=True,null=False)
    name = models.CharField(max_length=60)    
    
    def __str__(self):
        return self.name

class branches(models.Model):
    ifsc = models.CharField(max_length=11, null= False)
    bank_id = models.ForeignKey(bank, on_delete = models.CASCADE)
    branch = models.CharField(max_length=100) 
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.ifsc


    
    
