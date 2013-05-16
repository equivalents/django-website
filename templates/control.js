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
  

  


