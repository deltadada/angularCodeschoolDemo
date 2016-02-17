FROM TUTORIAL:

campus.codeschool.com/courses/shaping-up-with-angular-js/



FIRST STEPS

django-admin startproject angdemo 
cd angdemo
python manage.py startapp gemstore
python manage.py runserver
python manage.py makemigrations gemstore
python manage.py migrate

python manage.py inspectdb

python manage.py loaddata initial_data


Loads db with initial data from angdemo/gemstore/fixtures/initial_data.json
python manage.py loaddata initial_data



cd C:\gitrepo\angular_demo\angularCodeschoolDemo\angdemo\
python manage.py runserver  




SELECT 
	gemstore_gems.name,
	gemstore_gems.price,
	gemstore_gems.description,
	gemstore_gemimgs.url, 
	gemstore_gemimgtypes.imgType  
FROM 
	gemstore_gems
	INNER JOIN
	gemstore_gemimgs
ON
	gemstore_gemimgs.gem_id = gemstore_gems.gems_id

	INNER JOIN 
	gemstore_gemimgtypes 
	ON 
	gemstore_gemimgs.imgType_id = gemstore_gemimgtypes.gemImgTypes_id 
AND 
	gemstore_gemimgtypes.imgType = 'THUMB'
 


from gemstore.models import Gems
from gemstore.models import GemImgs
from gemstore.models import GemImgTypes
from gemstore.models import Reviews


gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')

imgs = GemImgs.objects.prefetch_related('gem')

imgsindex = GemImgs.objects.prefetch_related('gem').filter(imgType = 1)
imgsindex[0].imgType.imgType


~~~~~

thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') // this is django for WHERE  -- see field lookup

thumbimgs = GemImgs.objects.prefetch_related('gem').filter(imgType = thumb)

for img in thumbimgs:
	print(img.url)
[prints thumb urls only]

imgs = GemImgs.objects.prefetch_related('gem')

for img in thumbimgs:
	print(img.gem.name)
[prints gem names]

~~~~~~
gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')
len(gems_avail) # 3
thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') # this is django for WHERE  -- see field lookup
thumbimgs = GemImgs.objects.prefetch_related('gem').filter(imgType = thumb)
for displayGem in thumbimgs:
	print(displayGem.gem.name, displayGem.gem.description, displayGem.gem.price, displayGem.gem.soldOut, displayGem.url)
# displays all gems (incl soldout = true) with only thumb urls

~~~~~~
gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')
len(gems_avail) # 3 -- correct
thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') # WHERE in django  -- see field lookup
availGemDisplay = GemImgs.objects.filter(imgType = thumb).prefetch_related('gem').filter(gem = gems_avail)
len(availGemDisplay) # 1 - should have 3 of 4
for img in availGemDisplay:
	print(img.gem.name, img.gem.description, img.gem.price, img.gem.soldOut, img.url)
# only returns first row of gems where soldOut = false
~~~~~~
gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')
len(gems_avail) # 3 -- correct
thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') # WHERE in django  -- see field lookup
thumbimgs = GemImgs.objects.prefetch_related('gem').filter(imgType = thumb)
len(thumbimgs) # 4 correct
availGemDisplay = thumbimgs.prefetch_related('gem').filter(gem = gems_avail)
len(availGemDisplay)
for img in availGemDisplay:
	print(img.gem.name, img.gem.soldOut, img.url)
~~~~~~
gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')
len(gems_avail) # 3 -- correct
thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') # WHERE in django  -- see field lookup
thumbimgs = GemImgs.objects.prefetch_related('gem').filter(imgType = thumb)
len(thumbimgs) # 4 correct
availGemDisplay = thumbimgs.objects.all().filter(gem = gems_avail)
len(availGemDisplay)
for img in availGemDisplay:
	print(img.gem.name, img.gem.soldOut, img.url)

~~~~~~
availGemDisplay = Gems.objects.filter(soldOut=False).filter(canPurchase=True).filter(gemimgs__imgTypeChar = 'B')
for img in availGemDisplay:
	print(img.name, img.soldOut)


~~~~~~
gems_avail = Gems.objects.all().filter(canPurchase = True).filter(soldOut = False).order_by('price')
len(gems_avail) # 3 -- correct
thumb = GemImgTypes.objects.get(imgType__exact = 'THUMB') # WHERE in django  -- see field lookup
thumbimgs = gems_avail.prefetch_related('gemimgs').filter(gemimgs__imgType = thumb)
dir(thumbimgs)

len(thumbimgs) # 4 correct
availGemDisplay = thumbimgs.objects.all().filter(gem = gems_avail)
len(availGemDisplay)
for img in thumbimgs:
	print(img.gem.name, img.gem.soldOut, img.url)

~~~~~~

availGems = Gems.available(Gems.objects.all())

for displayGem in availGems:
	print(displayGem.name, " | ", displayGem.description, " | ",  displayGem.price, " | ",  displayGem.soldOut)


availGems_ID = Gems.available(Gems.objects.all()).values_list('gems_id', flat = True)

print(availGems.query)

thumbimgs = GemImgs.thumbs(GemImgs.objects.prefetch_related(availGems))
for displayGem in thumbimgs:
	print(displayGem.gem.name, " | ", displayGem.gem.description, " | ",  displayGem.gem.price, " | ",  displayGem.gem.soldOut, " | ",  displayGem.url)

##available = GemImgs.objects.filter(gem__soldOut=False, gem__canPurchase=True, imgType__imgType = 'THUMB').values_list('gem__id', 'gem__name', 'gem__description','gem__price','url','gem__soldOut','gem__canPurchase').distinct('gem__id') # not supported


available = GemImgs.objects.filter(gem__soldOut=False, gem__canPurchase=True, imgType__imgType = 'THUMB')
for i in available:
    print(i.gem.name, i.gem.soldOut, i.gem.canPurchase, i.url)






