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


gems_all = Gems.objects.all().select_related('GemImgs').filter(canPurchase = True).filter(soldOut = False).order_by('price')

g = GemImgs.objects.prefetch_related('gem')

g = GemImgs.objects.prefetch_related('gem').filter(imgType = 1)
g[0].imgType.imgType

g = GemImgs.objects.prefetch_related('gem').filter(imgType.imgType = 'THUMB')
g[0].imgType.imgType

