'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.factory('graphsService', function($http) {
  var graphsService = {
    getTopUsers: function() {
      var promise = $http.get('http://10.30.0.33:8080/top_users').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    },
    getTopArtists: function() {
      var promise = $http.get('http://10.30.0.33:8080/top_artists').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    }
  };
  return graphsService;
});
