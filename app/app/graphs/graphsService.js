'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.factory('graphsService', function($http) {
  var graphsService = {
    getTopUsers: function() {
      var promise = $http.get('http://10.11.4.160:8080/top_users').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    },
    getTopArtists: function() {
      var promise = $http.get('http://10.11.4.160:8080/top_artists').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    },
    getTopTracks: function() {
      var promise = $http.get('http://10.11.4.160:8080/top_tracks').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    },
    getTopTags: function() {
      var promise = $http.get('http://10.11.4.160:8080/top_tags').then(function (response) {
        console.log(response);
        return response.data;
      });
      return promise;
    }
  };
  return graphsService;
});
