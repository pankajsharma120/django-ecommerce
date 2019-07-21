from django.db import models
from django.db.models.signals import pre_save
import datetime
from .utils import unique_slug_generator
import random
import os
from seller.models import SellerProfileModel
from locations.models import Location
# functions

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):

    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "product/media/images/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


# Local models



class ProductCreateModel(models.Model):
    def get_pincode(self):
        return self.Location.pincode
    Seller          = models.ForeignKey(SellerProfileModel,related_name='product_create')
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(unique=True,blank=True)
    description     = models.TextField(max_length=250)
    price           = models.DecimalField(decimal_places=2, max_digits=7)
    image           = models.ImageField(upload_to=upload_image_path)
    active          = models.BooleanField(default=True)
    stock           = models.PositiveIntegerField()
    brand_name      = models.CharField(max_length=120)
    model_name      = models.CharField(max_length=120,blank=True,null=True)
    model_number    = models.CharField(max_length=120,blank=True,null=True)
    colour          = models.CharField(max_length=120,blank=True,null=True)
    warranty        = models.BooleanField(default=True)
    publish_date    = models.DateTimeField(auto_now_add=True)
    #Inhrited
    product_location= models.ForeignKey(Location, related_name = 'product_location')


    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=ProductCreateModel)
pre_save.connect(product_pre_save_receiver, sender=Location)
