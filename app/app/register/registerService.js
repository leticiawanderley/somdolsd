'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.factory('registerService', function($http) {
  var registerService = {
    addUsername: function(user) {
      var config = [];
      var promise = $http.post('/add', user, config).then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    }
  };
  return registerService;
});
