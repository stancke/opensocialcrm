$(document).ready(function() {
				
	$( "#tabs" ).tabs();
	$( ".lead").click(function(){
		var nome  = $(this).attr('nome');
		var twitter = $(this).attr('twitter');
		var facebook = $(this).attr('facebook');
		var linkedin = $(this).attr('linkedin');
		var id = $(this).attr('rel');
	
		$.ajax({
		   type: "POST",
		   url: "/sistema/leads/adicionar/",
		   data: "nome=" + nome + "&twitter=" + twitter + "&facebook=" + facebook + "&linkedin=" + linkedin,
		   dataType: "json",
		   success: function(json){
			 if (json.adicionado == true){
			 	$("#adicionar"+id).attr("src", "");
			 	$("#adicionado"+id).attr("src","/media/images/icons/accept.png");
			 }
		   }
		 });
	});
				
});