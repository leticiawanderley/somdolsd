'use strict';

var somDoLSD = angular.module('somDoLSD');
somDoLSD.controller('graphsController', function($scope, graphsService) {
  var vm = this;
  vm.options = {width: 500, height: 300, 'bar': 'aaa'};
  vm.topUsers = [];
  vm.topArtists = [];
  vm.topTracks = [];
  vm.topTags = [];
  graphsService.getTopUsers().then(
    function(d) {
      vm.topUsers = d;
    },
    function(d) {
      vm.topUsers = [];
    });

  graphsService.getTopArtists().then(
    function(d) {
      vm.topArtists = d;
    },
    function(d) {
      vm.topArtists = [];
    }
  );
  graphsService.getTopTracks().then(
    function(d) {
      vm.topTracks = d;
    },
    function(d) {
      vm.topTracks = [];
    });

  graphsService.getTopTags().then(
    function(d) {
      vm.topTags = d;
    },
    function(d) {
      vm.topTags = [];
    }
  );
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

somDoLSD.directive('barChartTracks', function(){
  var chart = d3.custom.barChart();
    return {
      restrict: 'E',
      replace: true,
      template: '<div id="tracks" class="tracks"></div>',
      scope:{
        height: '=height',
        data: '=data'
      },
      link: function(scope, element, attrs) {
        var chartEl = d3.select("#tracks");
        scope.$watch('data', function (newVal, oldVal) {
          chartEl.datum(newVal).call(chart);
        });
        scope.$watch('height', function(d, i){
          chartEl.call(chart.height(scope.height));
        })
      }
    }
});

somDoLSD.directive('barChartTags', function(){
  var chart = d3.custom.barChart();
    return {
      restrict: 'E',
      replace: true,
      template: '<div id="tags" class="tags"></div>',
      scope:{
        height: '=height',
        data: '=data'
      },
      link: function(scope, element, attrs) {
        var chartEl = d3.select("#tags");
        scope.$watch('data', function (newVal, oldVal) {
          chartEl.datum(newVal).call(chart);
        });
        scope.$watch('height', function(d, i){
          chartEl.call(chart.height(scope.height));
        })
      }
    }
})
