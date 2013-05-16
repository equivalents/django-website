
$(function (){
  $("#gpio_form").submit(function gpio_submit(){
    $("#gpio_results").load("/gpio_control/");
	return false;
  });
});