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

def db_dump(request):
    title = "Dump1"
    testString = "test"
    #gems_all2 = Gems.objects.all().prefetch_related('Reviews').order_by('stars')
    gems_all = Gems.objects.all().order_by('price')
    return render(request, './gemstore/dump.html', {'title' : title, 'gems_all':gems_all})

def index(request):
    return HttpResponse("Hello, world. You're at the gemstore index.")

def test(request):
    return HttpResponse("hello world")
