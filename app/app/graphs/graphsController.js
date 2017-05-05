'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('graphsController', function($scope, graphsService) {
  var vm = this;
  vm.options = {width: 500, height: 300, 'bar': 'aaa'};
  vm.topUsers = [];
  vm.topArtists = [];

  graphsService.getTopUsers().then(function(d) {
      vm.topUsers = d;
  });

  graphsService.getTopArtists().then(function(d) {
      vm.topArtists = d;
  });
});

somDoLSD.directive('barChartUsers', function(){
  var chart = d3.custom.barChart();
    return {
      restrict: 'E',
      replace: true,
      template: '<div id="users" class="users"></div>',
      scope:{
        height: '=height',
        data: '=data'
      },
      link: function(scope, element, attrs) {
        var chartEl = d3.select("#users");
        scope.$watch('data', function (newVal, oldVal) {
          chartEl.datum(newVal).call(chart);
        });
        scope.$watch('height', function(d, i){
          chartEl.call(chart.height(scope.height));
        })
      }
    }
});

somDoLSD.directive('barChartArtists', function(){
  var chart = d3.custom.barChart();
    return {
      restrict: 'E',
      replace: true,
      template: '<div id="artists" class="artists"></div>',
      scope:{
        height: '=height',
        data: '=data'
      },
      link: function(scope, element, attrs) {
        var chartEl = d3.select("#artists");
        scope.$watch('data', function (newVal, oldVal) {
          chartEl.datum(newVal).call(chart);
        });
        scope.$watch('height', function(d, i){
          chartEl.call(chart.height(scope.height));
        })
      }
    }
})
