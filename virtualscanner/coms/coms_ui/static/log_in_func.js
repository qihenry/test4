$(document).ready(function(){
  $("#standard-about").show();
  $("#advanced-about").hide();
  $("#test-about").hide();
});
$(document).on("click",".mode-option",function(){
  if ($(this).val() == "Standard") {
    $("#standard-about").show();
    $("#advanced-about").hide();
    $("#test-about").hide();
  }
  else if ($(this).val() == "Advanced") {
    $("#standard-about").hide();
    $("#advanced-about").show(); 
    $("#test-about").hide();
  }
  else{
    $("#standard-about").hide();
    $("#advanced-about").hide(); 
    $("#test-about").show();
  }

});
