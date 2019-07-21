from django.db import models
from product.utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.
# Foreign models

class Location(models.Model): #Must be populated by Company!!
    pincode         = models.IntegerField()
    slug            = models.SlugField(unique=True,blank=True)
    region_name     = models.CharField(max_length=250)
    district_name   = models.CharField(max_length=250)
    state_name      = models.CharField(max_length=250)
    pincode_str     = str(pincode)
    def get_absolute_url(self):
        return reverse("products:location_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return '{pincode_str}, {region_name}, {district_name}, {state_name}'.format(
                            pincode_str=self.pincode,region_name=self.region_name,
                            district_name=self.district_name,state_name=self.state_name)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Location)
