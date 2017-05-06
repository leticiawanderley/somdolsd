d3.custom = {};

d3.custom.barChart = function module() {
    var margin = {top: 20, right: 20, bottom: 40, left: 40},
        width = 500,
        height = 500,
        gap = 0,
        ease = 'cubic-in-out';
    var svg, duration = 500;

    function selectTop5(data) {
      data.sort(function(a, b) {
          return parseFloat(b.playcount) - parseFloat(a.playcount)
      });
      return data.slice(0, 5);
    };

    function userOrName(d) {
      return ((d.user) ? d.user : d.name) + ' ' +
        ((d.artist_name) ? d.artist_name : ' ');
    };

    function exports(_selection) {
        _selection.each(function(_data) {
            _data = selectTop5(_data);
            var chartW = width - margin.left - margin.right,
                chartH = height - margin.top - margin.bottom;

            var x1 = d3.scale.ordinal()
                .domain(_data.map(function(d, i){ return userOrName(d)}))
                .rangeRoundBands([0, chartW], .1);

            var y1 = d3.scale.linear()
                .domain([0, d3.max(_data, function(d, i){ return d.playcount; })])
                .range([chartH, 0]);

            var xAxis = d3.svg.axis()
                .scale(x1)
                .orient('bottom');

            var yAxis = d3.svg.axis()
                .scale(y1)
                .orient('left');

            var barW = chartW / _data.length;

            if(!svg) {
                svg = d3.select(this)
                    .append('svg');
                var container = svg.append('g').classed('container-group', true);
                container.append('g').classed('chart-group', true);
                container.append('g').classed('x-axis-group axis', true);
                container.append('g').classed('y-axis-group axis', true);
            }

            svg.transition().duration(duration).attr({width: width, height: height})
            svg.select('.container-group')
                .attr({transform: 'translate(' + margin.left + ',' + margin.top + ')'});

            svg.select('.x-axis-group.axis')
                .attr({transform: 'translate(-10,' + (chartH - 60) + ')'})
                .call(xAxis);

            svg.select('.y-axis-group.axis')
                .transition()
                .duration(duration)
                .ease(ease)
                .call(yAxis);

            svg.selectAll('.x-axis-group.axis text') // select all the x tick texts
              .style("text-anchor", "end")
              .attr("transform", function(d) {
                  return "rotate(-65)"
              })
              .call(function(t){
                 t.each(function(d){ // for each one
                   var self = d3.select(this);
                   var s = self.text().split(' ');  // get the text and split it
                   self.text(''); // clear it out
                   self.append("tspan") // insert two tspans
                     .attr("x", 0)
                     .attr("dy",".8em")
                     .text(s[0]);
                   self.append("tspan")
                     .attr("x", 0)
                     .attr("dy",".8em")
                     .text(s[1]);
                 })
               });

            var gapSize = x1.rangeBand() / 100 * gap;
            var barW = x1.rangeBand() - gapSize;
            var bars = svg.select('.chart-group')
                .selectAll('.bar')
                .data(_data);
            bars.enter().append('rect')
                .classed('bar', true)
                .attr({x: chartW,
                    width: barW,
                    y: function(d, i) { return y1(d.playcount); },
                    height: function(d, i) { return chartH - (10 + y1(d.playcount)) }
                });
            bars.transition()
                .duration(duration)
                .ease(ease)
                .attr({
                    width: barW,
                    x: function(d, i) { return x1(userOrName(d)) + gapSize/2; },
                    y: function(d, i) { return y1(d.playcount); },
                    height: function(d, i) { return chartH - (10 + y1(d.playcount)); }
                });
            bars.exit().transition().style({opacity: 0}).remove();

            duration = 500;

        });
    }
    exports.width = function(_x) {
        if (!arguments.length) return width;
        width = parseInt(_x);
        return this;
    };
    exports.height = function(_x) {
        if (!arguments.length) return height;
        height = parseInt(_x);
        duration = 0;
        return this;
    };
    exports.gap = function(_x) {
        if (!arguments.length) return gap;
        gap = _x;
        return this;
    };
    exports.ease = function(_x) {
        if (!arguments.length) return ease;
        ease = _x;
        return this;
    };
    return exports;
};
