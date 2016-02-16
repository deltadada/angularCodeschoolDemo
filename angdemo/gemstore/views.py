from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from gemstore.models import Gems
from gemstore.models import Reviews
from gemstore.models import GemImgs

# Create your views here.
def home(request):
    title = "Home"
    return render(request, './gemstore/index.html', {'title' : title})

def django_db_dump(request):
    title = "All Available Gems"
    testString = "test"
    gems_all = GemImgs.objects.filter(gem__soldOut=False, gem__canPurchase=True, imgType__imgType = 'THUMB')
    return render(request, './gemstore/django_db_dump.html', {'title' : title, 'gems_all':gems_all})

def index(request):
    return HttpResponse("Hello, world. You're at the gemstore index.")

def test(request):
    return HttpResponse("hello world")


