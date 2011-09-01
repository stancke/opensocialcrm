var chart;
var chart2;
			$(document).ready(function() {
				
				chart = new Highcharts.Chart({
					chart: {
						renderTo: 'div_container',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Citações da campanha por rede social'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
								}
							}
						}
					},
				    series: [{
						type: 'pie',
						name: 'Browser share',
						data: [
							['Twitter',   25.0],
							['LinkedIn',    8.5],
							['Facebook',     6.2]
						]
					}]
				});
				
				////////////////////
				///////////////////
				/////////////////////
				chart2 = new Highcharts.Chart({
					chart: {
						renderTo: 'div_container2',
						defaultSeriesType: 'column'
					},
					title: {
						text: 'Citações da campanha por tempo'
					},
					xAxis: {
						categories: [
							'Jan', 
							'Feb', 
							'Mar', 
							'Apr', 
							'May', 
							'Jun', 
							'Jul', 
							'Aug', 
							'Sep', 
							'Oct', 
							'Nov', 
							'Dec'
						]
					},
					yAxis: {
						min: 0,
						title: {
							text: 'Quantidade de Citações'
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
								this.x +': '+ this.y +' citações';
						}
					},
					plotOptions: {
						column: {
							pointPadding: 0.2,
							borderWidth: 0
						}
					},
				        series: [{
						name: 'Facebook',
						data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
				
					}, {
						name: 'Twitter',
						data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]
				
					}, {
						name: 'LinkedIn',
						data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]
				
					}]
				});
				
				/////////////////////
				/////////////////////
				////////////////////
				
				chart = new Highcharts.Chart({
					chart: {
						renderTo: 'div_container3',
						plotBackgroundColor: null,
						plotBorderWidth: null,
						plotShadow: false
					},
					title: {
						text: 'Aceitação da campanha por sexo'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
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
									return '<b>'+ this.point.name +'</b>: '+ this.y +' %';
								}
							}
						}
					},
				    series: [{
						type: 'pie',
						name: 'Browser share',
						data: [
							['Homem',   70],
							['Mulher',    30]
						]
					}]
				});
				
				/////////////////
				/////////////////
				////////////////
				
				chart = new Highcharts.Chart({
					chart: {
						renderTo: 'div_container4',
						margin: [50, 0, 0, 0],
						plotBackgroundColor: 'none',
						plotBorderWidth: 0,
						plotShadow: false				
					},
					title: {
						text: 'Aceitação da campanha por faixa etária'
					},
					tooltip: {
						formatter: function() {
							return '<b>'+ this.series.name +'</b><br/>'+ 
								this.point.name +': '+ this.y +' %';
						}
					},
				    series: [{
						type: 'pie',
						name: 'Twitter',
						size: '45%',
						innerSize: '20%',
						data: [
							{ name: '10-18 anos', y: 44.2, color: '#4572A7' },
							{ name: '19-25 anos', y: 46.6, color: '#AA4643' },
							{ name: '26-30 anos', y: 3.1, color: '#89A54E' },
							{ name: '31-40 anos', y: 2.7, color: '#80699B' },
							{ name: '41-50 anos', y: 2.3, color: '#3D96AE' },
							{ name: '60+ anos', y: 0.4, color: '#DB843D' }
						],
						dataLabels: {
							enabled: false
						}
					}, {
						type: 'pie',
						name: 'Facebook',
						innerSize: '45%',
						data: [
							{ name: '10-18 anos', y: 45.0, color: '#4572A7' },
							{ name: '19-25 anos', y: 26.8, color: '#AA4643' },
							{ name: '26-30 anos', y: 12.8, color: '#89A54E' },
							{ name: '31-40 anos', y: 8.5, color: '#80699B' },
							{ name: '41-50 anos', y: 6.2, color: '#3D96AE' },
							{ name: '60+ anos', y: 0.2, color: '#DB843D' }
						],
						dataLabels: {
							enabled: true,
							color: '#000000',
							connectorColor: '#000000'
						}
					}]
				});
			})