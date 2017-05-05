'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('mainController', function($location) {
  var vm = this;
  vm.mainPage = function() {
    $location.url("/");
  }

  vm.register = function() {
    $location.url("/register");
  }
});
