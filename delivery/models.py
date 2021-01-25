from django.db import models
from django.http import request
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.deconstruct import deconstructible

class Post(models.Model):
    categoryChoices = [
        ('HOME_APPLIANCES','Home Appliances'),
        ('SMARTPHONES', 'Smart Phones'),
        ('LAPTOPS','Laptops'),
        ('TABLETS','Tablets'),
        ('BOOKS','Books'),
        ('SPORTS/OUTDOOR','Sports and Outdoor'),
        ('CLOTHING','Clothing'),
        ('FURNITURE','Furniture'),
        ('OTHER','Other')
    ]
    conditionChoices = [
        ('NEW', 'New'),
        ('LIKE NEW', 'Like New'),
        ('FAIR', 'Fair'),
        ('ACCEPTABLE', 'Acceptable'),
        ('POOR', 'Poor')
    ]
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=17)
    title = models.CharField(max_length=100, blank=False)
    zip = models.CharField(max_length=200,default="", blank=False)
    email = models.CharField(max_length=100,default="email")
    name = models.CharField(max_length=100, blank=False, default="name")
    description = models.CharField(max_length=100, blank=False, default="")
    price = models.PositiveSmallIntegerField(blank=False, default=0)
    images = models.ImageField(upload_to='../media/ads/',blank=False, default='../media/default-img.gif')
    category = models.CharField(max_length=100,choices=categoryChoices,blank=False,default='OTHER')
    datePosted = models.DateTimeField(default=datetime.now(), blank=True)
    condition = models.CharField(max_length=10,choices=conditionChoices,blank=False,default='FAIR')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})