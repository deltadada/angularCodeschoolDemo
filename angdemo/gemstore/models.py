from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid
from django.utils import timezone

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# Create your models here.
class Gems(models.Model):
	id = models.AutoField(primary_key=True, blank=False, null=False)
	name = models.CharField(max_length = 255, blank=False, null=False )
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, default="0.00")
	description = models.CharField(max_length = 1056, blank=True, null=True )
	canPurchase = models.BooleanField(default = False)
	soldOut = models.BooleanField(default = False )

	def available(self, **kwargs):
		return self.filter(canPurchase=True, soldOut=False)

class Reviews(models.Model):
	id = models.AutoField(primary_key=True, blank=False, null=False)
	gem = models.ForeignKey(Gems, on_delete=models.CASCADE, blank=True, null=False) #one Gem to many Reviews
	stars = models.SmallIntegerField(blank=False, null=False, default=1)
	body = models.CharField(max_length=800, blank=False, null=False, default="...")
	author = models.CharField(max_length=254, blank=False, null=False, default="george@internet.com")

# class GemImgTypes(models.Model):
# 	id = models.AutoField(primary_key=True, blank=False, null=False)
# 	imgType = models.CharField(max_length=32, blank=False, null=False, unique=True)

class ThumbDisplays(models.Model):
	id = models.AutoField(primary_key=True, blank=False, null=False)
	gem = models.OneToOneField(Gems, on_delete=models.CASCADE, null=True)#one to one Gems
	url = models.URLField(max_length = 2000, blank=False, null=False, default="assets/img/noImage_th.png" )

	def name(self, **kwargs):
		return self.gem.name

	def price(self, **kwargs):
		return self.gem.price

	def description(self, **kwargs):
		return self.gem.description

class FullDisplays(models.Model):
	id = models.AutoField(primary_key=True, blank=False, null=False)
	gem = models.OneToOneField(Gems, on_delete=models.CASCADE, null=True)#one to one Gems
	url = models.URLField(max_length = 2000, blank=False, null=False, default="assets/img/noImage.png" )


# rest framework tutorial	
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)