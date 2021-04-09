$(document).ready(function() {

	$(".fa-search").click(function() {
		console.log("search click event");
	   $(".togglesearch").toggle();
	   $("input[type='text']").focus();
	 });

});
