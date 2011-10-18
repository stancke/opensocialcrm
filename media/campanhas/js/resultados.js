var chart;
var chart2;
			$(document).ready(function() {
				$(function() {
					$( "#tabs" ).tabs();
				});
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.locais').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.locais').each(function(index) {
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
						renderTo: 'div_locais',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Origem dos Visitantes (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_locais_barra',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Origem dos Visitantes (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////
				///////////////
				////////////////

				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.browsers').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.browsers').each(function(index) {
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
						renderTo: 'div_browsers',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_browsers_barra',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
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
								this.x +': '+ this.y +' visitas';
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
				
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.plataformas').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.plataformas').each(function(index) {
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
						renderTo: 'div_plataformas',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Plataforma (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_plataformas_barra',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Plataforma (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.paises').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.paises').each(function(index) {
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
						renderTo: 'div_paises',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por País (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_paises_barra',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por País (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
			
				
				
				///////////////////////////////////
				//////////////////////////////////
				/////////////////////////////////
				/////////MES/////////////////////
				
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.locais_mes').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.locais_mes').each(function(index) {
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
						renderTo: 'div_locais_mes',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Origem dos Visitantes (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_locais_barra_mes',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Origem dos Visitantes (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////
				///////////////
				////////////////

				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.browsers_mes').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.browsers_mes').each(function(index) {
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
						renderTo: 'div_browsers_mes',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_browsers_barra_mes',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
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
								this.x +': '+ this.y +' visitas';
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
				
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.plataformas_mes').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.plataformas_mes').each(function(index) {
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
						renderTo: 'div_plataformas_mes',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Plataforma (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_plataformas_barra_mes',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Plataforma (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.paises_mes').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.paises_mes').each(function(index) {
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
						renderTo: 'div_paises_mes',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por País (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_paises_barra_mes',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por País (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////////////////////
				////////////////////////////////
				///////////////////DIA//////////
				/////////////////////////////////
				/////////////////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.locais_dia').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.locais_dia').each(function(index) {
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
						renderTo: 'div_locais_dia',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Origem dos Visitantes (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_locais_barra_dia',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Origem dos Visitantes (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////
				///////////////
				////////////////

				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.browsers_dia').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.browsers_dia').each(function(index) {
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
						renderTo: 'div_browsers_dia',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_browsers_barra_dia',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
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
								this.x +': '+ this.y +' visitas';
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
				
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.plataformas_dia').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.plataformas_dia').each(function(index) {
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
						renderTo: 'div_plataformas_dia',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Plataforma (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_plataformas_barra_dia',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Plataforma (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.paises_dia').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.paises_dia').each(function(index) {
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
						renderTo: 'div_paises_dia',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por País (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_paises_barra_dia',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por País (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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

				
				//////////////////////////////////////
				///////////////////////////////////
				////////////////2 HORAS////////////////////
				//////////////////////////////////////////
				
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.locais_hora').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.locais_hora').each(function(index) {
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
						renderTo: 'div_locais_hora',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Origem dos Visitantes (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_locais_barra_hora',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Origem dos Visitantes (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////
				///////////////
				////////////////

				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.browsers_hora').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.browsers_hora').each(function(index) {
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
						renderTo: 'div_browsers_hora',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_browsers_barra_hora',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Browser (Percentual)'
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
								this.x +': '+ this.y +' visitas';
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
				
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.plataformas_hora').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.plataformas_hora').each(function(index) {
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
						renderTo: 'div_plataformas_hora',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por Plataforma (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_plataformas_barra_hora',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por Plataforma (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
				
				///////////////////
				////////////////////
				////////////////////
				
				dados = [];
				series = [];
				
				var qtd_total = 0;
				
				$('.paises_hora').each(function(index) {
    				var valor = $(this).val();
    				var qtd = parseInt($(this).attr('count'));
    				
    				qtd_total += qtd;
    				
    				
  				});
				
				
				
				$('.paises_hora').each(function(index) {
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
						renderTo: 'div_paises_hora',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Visitas por País (Percentual)'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +'% visita (s)';
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
						renderTo: 'div_paises_barra_hora',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Visitas por País (Quantidade)'
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
								this.x +': '+ this.y +' visitas';
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
