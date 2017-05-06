'use strict';

// Declare app level module which depends on views, and components
angular.module('somDoLSD', [
  'ngRoute',
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
  .when('/groups', {
  		templateUrl: 'groups/groups.html',
	    controller: 'groupsController'
	})
  .otherwise({redirectTo: '/'});
}]);
