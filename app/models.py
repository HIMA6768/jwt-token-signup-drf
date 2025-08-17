from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class gallery(models.Model):
    imgname=models.CharField(max_length=25)
    no=models.IntegerField()
    user= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.imgname
    
