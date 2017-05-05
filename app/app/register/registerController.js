'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('registerController', function(registerService) {
  var vm = this;
  vm.add = function() {
    registerService.addUsername(vm.username);
  }
});
