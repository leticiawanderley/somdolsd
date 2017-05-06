'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('mainController', function($location) {
  var vm = this;
  vm.itens =['2', '3', '4', '5'];

  vm.mainPage = function() {
    $location.url("/");
  }

  vm.register = function() {
    $location.url("/register");
  }

  vm.groups = function() {
    $location.url("/groups");
  }
});
