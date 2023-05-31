$(document).ready(function() {
  
    $('input[type="range"]').on("change mousemove", function() {
      $(this).next().html($(this).val());
    })
       
   });