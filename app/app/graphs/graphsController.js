'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('graphsController', function($scope, graphsService) {
  var vm = this;
  vm.options = {width: 500, height: 300, 'bar': 'aaa'};
  vm.topUsers = [{
    "hotness": 59,
    "index": 2,
    "user": "Listener"
  },
  {
    "hotness": 43,
    "index": 1,
    "user": "Cicranis"
  },
  {
    "hotness": 30,
    "index": 0,
    "user": "Fulano da Silva"
  },
  {
    "hotness": 30,
    "index": 5,
    "user": "Hackeador"
  },
  {
    "hotness": 25,
    "index": 3,
    "user": "Lorem Ipsum"
  },
  {
    "hotness": 11,
    "index": 4,
    "user": "Bla bla"
  },
  {
    "hotness": 12,
    "index": 4,
    "user": "Bla bla Bla"
  },
  {
    "hotness": 27,
    "index": 4,
    "user": "Outra pessoa"
  }];

  graphsService.getTopUsers().then(function(d) {
      vm.topUsers = d;
  });

  graphsService.getTopArtists().then(function(d) {
      vm.topArtists = d;
  });
});

somDoLSD.directive('barChart', function(){
          var chart = d3.custom.barChart();
            return {
                restrict: 'E',
                replace: true,
                template: '<div class="chart"></div>',
                scope:{
                    height: '=height',
                    data: '=data'
                },
                link: function(scope, element, attrs) {
                    var chartEl = d3.select(element[0]);
                    scope.$watch('data', function (newVal, oldVal) {
                        chartEl.datum(newVal).call(chart);
                    });

                    scope.$watch('height', function(d, i){
                        chartEl.call(chart.height(scope.height));
                    })
                }
            }
        })
