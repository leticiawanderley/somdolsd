'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('graphsController', function(graphsService) {
  var vm = this;
  graphsService.getTopUsers().then(function(d) {
      vm.topUsers = d;
  });

  graphsService.getTopArtists().then(function(d) {
      vm.topArtists = d;
  });
});
