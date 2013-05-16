<script type='text/javascript'>
  $(function (){
    $( "#slider_B" ).slider({
      range: "min",
      value: {{ sliderB.sliderValue }},
      min: 0,
      max: 100,
      stop: function( event, ui ) { 
        $( "#blue_power" ).val(ui.value );
		var blue_power =  $( "#blue_power" ).val();
		var data = { blue_power:blue_power };
		$.ajax({
		  url:"/slider/",
		  cache: "false",
          data:data	  
		});
      }	  
    });
    $( "#blue_power" ).val($( "#slider_B" ).slider( "value" ) );
	return false;
  });
  </script>
  
  <script type='text/javascript'>
  $(function (){
    $( "#slider_R" ).slider({
      range: "min",
      value: {{ sliderR.sliderValue }},
      min: 0,
      max: 100,
      stop: function( event, ui ) {
        $( "#red_power" ).val(ui.value );
		var red_power =  $( "#red_power" ).val();
		var data = { red_power:red_power };
		$.ajax({
		  url:"/slider/",
		  cache: "false",
          data:data	  
		});
      }	  
    });
    $( "#red_power" ).val($( "#slider_R" ).slider( "value" ) );
	return false;
  });
  </script>
  
  <script type='text/javascript'>
  $(function (){
    $( "#slider_G" ).slider({
      range: "min",
      value: {{ sliderG.sliderValue }},
      min: 0,
      max: 100,
      stop: function( event, ui ) {
        $( "#green_power" ).val(ui.value );
		var green_power =  $( "#green_power" ).val();
		var data = { green_power:green_power };
		$.ajax({
		  url:"/slider/",
		  cache: "false",
          data:data	  
		});
      }	  
    });
    $( "#green_power" ).val($( "#slider_G" ).slider( "value" ) );
	return false;
  });
  </script>
  
  <script type='text/javascript'>
  $(function (){
    $( "#slider_P" ).slider({
      range: "min",
      value: {{ sliderP.sliderValue }},
      min: 0,
      max: 100,
      stop: function( event, ui ) {
        $( "#phase_speed" ).val(ui.value );
		var phase_speed =  $( "#phase_speed" ).val();
		var data = { phase_speed:phase_speed };
		$.ajax({
		  url:"/slider/",
		  cache: "false",
          data:data	  
		});
      }	  
    });
    $( "#phase_speed" ).val($( "#slider_P" ).slider( "value" ) );  
	return false;
  });
  </script>
  
  <script type='text/javascript'>
  $(function (){
	$( "#phase_slider" ).click(function (){
	   $( "#slider_group" ).hide();
	   $( "#slider_P" ).show();
    });	   
	return false;
  });
  </script>
  
  <script type='text/javascript'>
  $(function (){
    $( "#phase_slider" ).hide();
	$( "#preprogams" ).hide();
	$( "#control_options" ).toggle(  
      function () {
	    $( "#slider_group"  ).hide();
	    $( "#phase_slider" ).show();
		$( "#preprogams"  ).hide();
	  },  
	  function () {
	    $( "#preprogams" ).show();
	    $( "#slider_group"  ).hide();
	    $( "#phase_slider" ).hide();
	  },
	  function () {
	    $( "#slider_group"  ).show();
	    $( "#phase_slider" ).hide();
		$( "#preprogams" ).hide();
		var green_power =  $( "#green_power" ).val();
		var red_power =  $( "#red_power" ).val();
		var blue_power =  $( "#blue_power" ).val();
		var data = { green_power:green_power, blue_power:blue_power, red_power:red_power };
		$.ajax({
		  url:"/slider/",
		  cache: "false",
          data:data	  
		});
	  }
    );	   
	return false;
  });
  </script>
 
<script type='text/javascript'> 
$(function (){
  $("#police").click(function (){
    if ($( "#police" ).val() == 'on'){
      $( "#police" ).val("off");
      var police =  $( "#police" ).val();
      var police_data = { police:police };
      $.ajax({
        url:"/slider/",
        cache: "false",
        data:police_data,	  
	    type: "GET"
      });
    }
    else{
      $( "#police" ).val("on");
      $( "#danger" ).val("off");
      var danger =  $( "#danger"  ).val();
      var police =  $( "#police" ).val();
      var police_danger_data = { police:police, danger:danger };
      $.ajax({
        url:"/slider/",
        cache: "false",
        data:police_danger_data,	  
	    type: "GET"
      });
    }	  
  });
  return false;
});
</script> 

<script type='text/javascript'> 
$(function (){
  $("#danger").click(function (){
    if ($( "#danger" ).val() == 'on'){
      $( "#danger" ).val("off");
    }
    else{
      $( "#danger" ).val("on");
      $( "#police" ).val("off");
    }	  
    var danger =  $( "#danger" ).val();
	var police =  $( "#police" ).val();
    var data = { police:police, danger:danger };
    $.ajax({
      url:"/slider/",
      cache: "false",
      data:data,	  
	  type: "GET"
    });
  });
  return false;
});
</script> 

<script type='text/javascript'> 
$(function (){
  $("#kill").click(function (){	
    $( "#danger" ).val("off");
    $( "#police" ).val("off");  
    var kill =  $( "#kill" ).val();
    var data = { kill:kill };
    $.ajax({
      url:"/slider/",
      cache: "false",
      data:data,	  
	  type: "GET"
    });
  });
  return false;
});
</script> 

