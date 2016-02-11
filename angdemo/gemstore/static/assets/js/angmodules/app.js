(function(){

var rootpath = "C:/gitrepo/angular_demo/django_angdemo/angdemo/gemstore/static/";
var app = angular.module('store', ['store-products']); // store depends on store-products

var app = angular.module('store').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});



// controller
app.controller('StoreController', function(){
	this.products = gems; // flat db stored in app.js
});


// controller replaced by directive
// app.controller('PanelController', function(){
// 	this.tab=1; // initialize tab in controller instead of ng-init
// 	// this.reviews = reviews;
	
// 	this.selectTab= function(setTab){
// 		this.tab = setTab;
// 	};

// 	this.isSelected=function(checkTab){
// 		return this.tab === checkTab;
// 	}

// });

// directive with controller
app.directive('productPanels', function(){
	return{
		restrict: 'E', // type: 'attribute' : goes in tag
		templateUrl: '../static/angcludes/product-panels.html',
		controller: function(){
			this.tab=1; // initialize tab in controller instead of ng-init
			// this.reviews = reviews;
			
			this.selectTab= function(setTab){
				this.tab = setTab;
			};

			this.isSelected=function(checkTab){
				return this.tab === checkTab;
			}
		},
		controllerAs: 'panel',
	};
});



app.controller("ReviewController", function(){ 
	this.review ={};

	this.addReview = function(product){
		//console.log(product);
		product.reviews.push(this.review);
		this.review = {};
	}
});

// ## these directives moved to 'store-product' dependency in product.js
// // directive -- convert tag-hyphen to camelCase directive name, e.g. productTitle

// app.directive('productTitle', function(){
// 	return{
// 		restrict: 'E', // type: 'element' is a tag
// 		templateUrl: '../static/angcludes/product-title.html',
// 	};
// });

// app.directive('productReviews', function(){
// 	return{
// 		restrict: 'E', // type: 'element' is a tag
// 		templateUrl: '../static/angcludes/product-reviews.html',
// 	};
// });

// app.directive('productDescription', function(){
// 	return{
// 		restrict: 'A', // type: 'attribute' : goes in tag
// 		templateUrl: '../static/angcludes/product-description.html',
// 	};
// });

// app.directive('productSpecs', function(){
// 	return{
// 		restrict: 'A', // type: 'attribute' : goes in tag
// 		templateUrl: '../static/angcludes/product-specs.html',
// 	};
// });

// app.directive('productReviewform', function(){
// 	return{
// 		restrict: 'A', // type: 'attribute' : goes in tag
// 		templateUrl: '../static/angcludes/product-reviewForm.html',
// 	};
// });

var reviews=[
{
	stars:5,
	body: "I love this gem!",
	author: "joe@joe.com",
},
{
	stars:4,
	body: "This is good.",
	author: "jill@egg.com",
},
{
	stars:3,
	body: "This is mediocre.",
	author: "lawrence@egg.com",
},
{
	stars:2,
	body: "This is laaaaaaaaaaaaame.",
	author: "brody@egg.com",
},
{
	stars:1,
	body: "This sucks.",
	author: "jasmine@egg.com",
},
];

var gems = [
	{
		name: 'Dodecahedron',
		price: 2.95,
		description: 'a nice gem',
		canPurchase: false,
		soldOut: true,
		images: [
			{full:'../static/assets/img/dec.png',
			thumb:'../static/assets/img/dec_th.png'},
		],
		reviews: reviews,
	},

	{
		name: 'Pentagonal',
		price: 33,
		description: 'a five-sided gem',
		canPurchase: false,
		soldOut: true,
		images: [
			{full:'../static/assets/img/pent.png',
			thumb:'../static/assets/img/pent_th.png'},
		],
		reviews: reviews,
	},

	{
		name: 'Round',
		price: 17.67,
		description: 'a round gem',
		canPurchase: false,
		soldOut: true,
		images: [
				{full:'../static/assets/img/round.png',
				thumb:'../static/static/assets/img/round_th.png'},
			],
		reviews: reviews,
	},
];



})();
