from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid
from django.utils import timezone


IMAGE_TYPES = (
    ('A', 'FULL'),
    ('B', 'THUMB'),
)

# Create your models here.
class Gems(models.Model):
	gems_id = models.AutoField(primary_key=True, blank=False, null=False)
	name = models.CharField(max_length = 255, blank=False, null=False )
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default="0.00")
	description = models.CharField(max_length = 1056, blank=True, null=True )
	canPurchase = models.BooleanField(default = False )
	soldOut = models.BooleanField(default = False )

	def available(self, **kwargs):
		return self.filter(canPurchase=True, soldOut=False)

class Reviews(models.Model):
	reviews_id = models.AutoField(primary_key=True, blank=False, null=False)
	gem = models.ForeignKey(Gems, on_delete=models.CASCADE, blank=True, null=False) #one Gem to many Reviews
	stars = models.SmallIntegerField(blank=False, null=False, default=1)
	body = models.CharField(max_length=800, blank=False, null=False, default="...")
	author = models.CharField(max_length=254, blank=False, null=False, default="george@internet.com")

class GemImgTypes(models.Model):
	gemImgTypes_id = models.AutoField(primary_key=True, blank=False, null=False)
	imgType = models.CharField(max_length=32, blank=False, null=False, unique=True)

class GemImgs(models.Model):
	gemImgs_id = models.AutoField(primary_key=True, blank=False, null=False)
	gem = models.ForeignKey(Gems, on_delete=models.CASCADE, blank=True, null=False) #one Gem to many  GemImgs
	imgType = models.ForeignKey(GemImgTypes, on_delete=models.PROTECT, null=True) #one GemImgType to many  GemImgs
	url = models.URLField(max_length = 2000, blank=False, null=False, default="image_not_avail.png" )
	imgTypeChar = models.CharField( max_length = 1, choices=IMAGE_TYPES) # link to array in models.py instead of table

	def thumbs(self, **kwargs):
		return self.filter(imgType = GemImgTypes.objects.get(imgType__exact = 'THUMB'))

	
