var chart;
var chart2;
$(document).ready(function() {
	$(function() {
		$( "#tabs_redes" ).tabs();
	});
	
	dados = [];
	series = [];
	
	var qtd_total = 0;
	
	$('.redes').each(function(index) {
		var valor = $(this).val();
		var qtd = parseInt($(this).attr('count'));
		
		qtd_total += qtd;
		
		
		});
	
	
	
	$('.redes').each(function(index) {
		var valor = $(this).val();
		var qtd = parseInt($(this).attr('count'));
		var result = qtd / qtd_total * 100;
		
		result = (Math.round(result*100))/100;
		
		if(qtd != 0){
			dados.push([valor, result]);
			
			series.push({
				name: valor,
				data: qtd
		
			});
		}
		});
	
		
	chart = new Highcharts.Chart({
		chart: {
			renderTo: 'div_redes',
			plotBackgroundColor: null,
			plotBorderWidth: null,
			plotShadow: false
		},
		title: {
			text: 'Redes Sociais (Percentual)'
		},
		tooltip: {
			formatter: function() {
				return '<b>'+ this.point.name +'</b>: '+ this.y +'% comentário (s)';
			}
		},
		plotOptions: {
			pie: {
				allowPointSelect: true,
				cursor: 'pointer',
				dataLabels: {
					enabled: true,
					color: '#000000',
					connectorColor: '#000000',
					formatter: function() {
						return '<b>'+ this.point.name +'</b>: '+ this.y +'% comentário (s)';
					}
				}
			}
		},
	    series: [{
			type: 'pie',
			name: 'Browser share',
			data:  dados 
		    
		}]
	});
	
	chart2 = new Highcharts.Chart({
		chart: {
			renderTo: 'div_redes_barra',
			defaultSeriesType: 'column'
		},
		title: {
			text: 'Redes Sociais (Quantidade)'
		},
		xAxis: {
			categories: [
				''
			]
		},
		yAxis: {
			min: 0,
			title: {
				text: 'Quantidade de Visitas'
			}
		},
		legend: {
			layout: 'vertical',
			backgroundColor: '#FFFFFF',
			align: 'left',
			verticalAlign: 'top',
			x: 100,
			y: 70,
			floating: true,
			shadow: true
		},
		tooltip: {
			formatter: function() {
				return ''+
					this.x +': '+ this.y +' comentários';
			}
		},
		plotOptions: {
			column: {
				pointPadding: 0.2,
				borderWidth: 0
			}
		},
	        series: series
	});
	
});
