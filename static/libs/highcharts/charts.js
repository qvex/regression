var priceObjs = document.getElementsByClassName('prices');
var yearObjs = document.getElementsByClassName('years');

var prices = []
var years = []

for (var i = 0; i < priceObjs.length; i++) {
    prices.push(parseFloat(priceObjs[i].innerHTML));
}

for (var i = 0; i < yearObjs.length; i++) {
    years.push(yearObjs[i].innerHTML);
}

var chart = Highcharts.chart('crop-pred', {
    title: {
        text: document.getElementById('title').innerHTML
    },

    xAxis: {
        categories: years
    },

    series: [{
        type: 'column',
        colorByPoint: true,
        data: prices,
        showInLegend: false
    }]

});

