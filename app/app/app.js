'use strict';

// Declare app level module which depends on views, and components
angular.module('somDoLSD', [
  'ngRoute',
  'ngSanitize'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');
  $routeProvider
  .when('/', {
  		templateUrl: 'graphs/graphs.html',
	    controller: 'graphsController'
	})
  .when('/register', {
  		templateUrl: 'register/register.html',
	    controller: 'registerController'
	})
  .otherwise({redirectTo: '/'});
}]);
