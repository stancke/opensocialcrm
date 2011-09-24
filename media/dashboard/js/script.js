$(document).ready(function() {
	
	$(function() {
		$( "#tabs" ).tabs();
	});
	
	$( ".column" ).sortable({
		connectWith: ".column"
	});
	
	$( ".portlet" ).addClass( "ui-widget ui-widget-content ui-helper-clearfix ui-corner-all" )
			.find( ".portlet-header" )
				.addClass( "ui-widget-header ui-corner-all" )
				.prepend( "<span class='ui-icon ui-icon-minusthick'></span>")
				.end()
			.find( ".portlet-content" );

		$( ".portlet-header .ui-icon" ).click(function() {
			$( this ).toggleClass( "ui-icon-minusthick" ).toggleClass( "ui-icon-plusthick" );
			$( this ).parents( ".portlet:first" ).find( ".portlet-content" ).toggle();
		});

	$( ".column" ).disableSelection();
	
	$("#twitter").tweet({
                join_text: "auto",
                username: "socialcrm1",
                avatar_size: 48,
                count: 3,
                loading_text: "carregando tweets..."
	});
});