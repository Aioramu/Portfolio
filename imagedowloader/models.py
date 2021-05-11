
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Gallery(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
class Image(models.Model):
    gallery = models.ForeignKey(Gallery,  related_name='Image',on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published',auto_now=True)
    path=models.ImageField(upload_to='')
