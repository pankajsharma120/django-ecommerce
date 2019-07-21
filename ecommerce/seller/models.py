from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from locations.models import Location
# from djangoratings.fields import RatingField
# Create your models here.

class SellerProfileModel(AbstractBaseUser):

    username       = models.CharField(max_length=120,unique=True)
    first_name     = models.CharField(max_length=120)
    last_name      = models.CharField(max_length=120)
    shop_name      = models.CharField(max_length=120)
    email          = models.EmailField(max_length=256,unique=True)
    is_active      = models.BooleanField(default=True)
    is_seller      = models.BooleanField(default=True)
    phone_number   = models.PositiveIntegerField()
    address        = models.ForeignKey(Location,related_name='seller_location')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('seller:profile', kwargs={'username': self.username})

    # rating         = RatingField(range=5,
    #                             can_change_vote=True,
    #                             allow_delete =True,
    #                             allow_anonymous =True,
    #                             use_cookies =True)
    def __str__(self):
        return self.username
