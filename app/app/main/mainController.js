'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('mainController', function($location) {
  var vm = this;
  vm.itens =['2', '3', '4', '5'];
  var source = new EventSource('/topic/test');
  source.addEventListener('message', function(e){
      console.log('Message: ');
      console.log(e.data);
  }, false);

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
