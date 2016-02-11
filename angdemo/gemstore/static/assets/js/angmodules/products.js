(function(){

// pulled out all the product directives and controllers -- new 'app' is 'store-products'
var app = angular.module('store-products', []);

//var rootpath = "C:/gitrepo/angular_demo/django_angdemo/angdemo/gemstore/static/";


// directive -- convert tag-hyphen to camelCase directive name, e.g. productTitle

app.directive('productTitle', function(){
	return{
		
		restrict: 'E', // type: 'element' is a tag
		templateUrl: '../static/angcludes/product-title.html',
	};
});

app.directive('productReviews', function(){
	return{
		restrict: 'E', // type: 'element' is a tag
		templateUrl: '../static/angcludes/product-reviews.html',
	};
});

app.directive('productDescription', function(){
	return{
		restrict: 'A', // type: 'attribute' : goes in tag
		templateUrl: '../static/angcludes/product-description.html',
	};
});

app.directive('productSpecs', function(){
	return{
		restrict: 'A', // type: 'attribute' : goes in tag
		templateUrl: '../static/angcludes/product-specs.html',
	};
});

app.directive('productReviewform', function(){
	return{
		restrict: 'A', // type: 'attribute' : goes in tag
		templateUrl: '../static/angcludes/product-reviewForm.html',
	};
});


})();
