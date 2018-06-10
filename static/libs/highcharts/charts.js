var priceObjs = document.getElementsByClassName('prices');
var yearObjs = document.getElementsByClassName('years');

var prices = []
for (var i = 0; i < priceObjs.length; i += 1) {
    prices.push(parseFloat(priceObjs[i].innerHTML));
}

var years = []
for (var i = 0; i < yearObjs.length; i += 1) {
    years.push(yearObjs[i].innerHTML);
}

//Bar Chart 
var chart = Highcharts.chart('crop-pred', {
    title: {
        text: document.getElementById('title').innerHTML
    },

    subtitle: {
        text: ''
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


$('#plain').click(function () {
    chart.update({
        chart: {
            inverted: false,
            polar: false
        },
        subtitle: {
            text: 'Plain'
        }
    });
});

$('#inverted').click(function () {
    chart.update({
        chart: {
            inverted: true,
            polar: false
        },
        subtitle: {
            text: 'Inverted'
        }
    });
});

$('#polar').click(function () {
    chart.update({
        chart: {
            inverted: false,
            polar: true
        },
        subtitle: {
            text: 'Polar'
        }
    });
});