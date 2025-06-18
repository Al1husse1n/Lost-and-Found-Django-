from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 
    
class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'lost'),  #First element of the tuple  is the actual value stored in the database. second is human readable name displayed in form/admin
        ('found','found')
    ]
    item_name = models.CharField(max_length=100)
    item_picture = models.ImageField(upload_to="Item_pictures/") #pip install Pillow
    item_description = models.TextField()
    item_founder = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='found_items')  #user_profile.found_items.all()
    contactEmail = models.EmailField()
    found_at = models.CharField(max_length=100)
    reported_datetime = models.DateTimeField(auto_now_add=True)
    found_datetime = models.DateTimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='lost')
    claimed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='claimed_items')

    def __str__(self):
        return self.item_name
    

      
        














