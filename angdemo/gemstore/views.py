from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from gemstore.serializers import ThumbsDisplaySerializer
from gemstore.serializers import GemsSerializer

from gemstore.models import Gems
from gemstore.models import Reviews
from gemstore.models import FullDisplays
from gemstore.models import ThumbDisplays

# Create your views here.
def home(request):
    title = "Home"
    return render(request, './gemstore/index.html', {'title' : title})

def django_db_dump(request):
    title = "All Available Gems"
    testString = "test"
    gems_all = ThumbDisplays.objects.filter(gem__soldOut=False, gem__canPurchase=True)

    return render(request, './gemstore/django_db_dump.html', {'title' : title, 'gems_all':gems_all})

def index(request):
    return HttpResponse("Hello, world. You're at the gemstore index.")

def test(request):
    return HttpResponse("hello world")

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def gems_list(request):
    """
    List all available Gems with url to Thumbnail
    """
    if request.method == 'GET':
        qGems = Gems.objects.filter(soldOut=False, canPurchase=True)
        serializer = GemsSerializer(qGems, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def gemsthumb_list(request):
    """
    List all available Gems with url to Thumbnail
    """
    if request.method == 'GET':
        qGemsAvailThumb = ThumbDisplays.objects.filter(gem__soldOut=False, gem__canPurchase=True)
        serializer = ThumbsDisplaySerializer(qGemsAvailThumb, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def availableGemsThumbs_list(request):
    """
    List all available Gems with url to Thumbnail
    """
    if request.method == 'GET':
        qGemsAvailThumb = ThumbDisplays.objects.filter(gem__soldOut=False, gem__canPurchase=True)
        data = serializers.serialize(
        	'json', list(qGemsAvailThumb), 
        	fields=('url','gems.name','gems.description')
        	)
        return JSONResponse(data)