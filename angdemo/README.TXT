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



<!-- 
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
 
 -->
