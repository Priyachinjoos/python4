from django.db import models

# Create your models here.
class Travel(models.Model):
    pic=models.ImageField(upload_to='pic')
    name=models.CharField(max_length=250)
    des=models.TextField()

def __str__(self):
    return self.pic
