'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('registerController', function(registerService) {
  var vm = this;
  vm.user = {
    username: '',
    name: '',
    sala: ''
  }
  vm.salas = ['Sapupara', 'Volúpia',
  'Dona Bica', 'Bruxaxá', 'Rainha',
  'Auditório São Paulo', 'Serra Preta',
  'Triunfo', 'Carvalheira', 'Serra Limpa',
  'Engenho do Meio', 'Ypióca', 'Caruçu'];
  vm.add = function() {
    registerService.addUser(vm.user);
  }
});
