$(document).ready(function() {
				
	$( ".campanha" ).click(function(){
		var id = $(this).attr('rel');
		$("#campanha").val(id);
		$('form').submit();
	});	
});