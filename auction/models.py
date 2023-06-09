from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuctionItems(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures/', max_length=100, default='default.jpg')
    description = models.TextField(blank=True)
    current_bid = models.IntegerField()
    number_of_hours = models.CharField(max_length=10, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    #bid_time = models.TimeField(blank=True, null=True)
    owner = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE, null=True)
    winner = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name
    
