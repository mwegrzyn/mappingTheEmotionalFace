
$(document).ready(function(){

  $("#startscreen").hide();


  var my_img = new Image();

  var all_img = ["app/static/img/MorphF01_cut.png",
  "app/static/img/MorphF02_cut.png",
  "app/static/img/MorphF03_cut.png",
  "app/static/img/MorphF04_cut.png",
  "app/static/img/MorphF05_cut.png",
  "app/static/img/MorphF06_cut.png",
  "app/static/img/MorphF07_cut.png",
  "app/static/img/MorphF08_cut.png",
  "app/static/img/MorphF09_cut.png",
  "app/static/img/MorphM01_cut.png",
  "app/static/img/MorphM02_cut.png",
  "app/static/img/MorphM03_cut.png",
  "app/static/img/MorphM04_cut.png",
  "app/static/img/MorphM05_cut.png",
  "app/static/img/MorphM06_cut.png",
  "app/static/img/MorphM07_cut.png",
  "app/static/img/MorphM08_cut.png",
  "app/static/img/MorphM09_cut.png",
  "app/static/img/MorphF01_cut_upper.png",
  "app/static/img/MorphF02_cut_upper.png",
  "app/static/img/MorphF03_cut_upper.png",
  "app/static/img/MorphF04_cut_upper.png",
  "app/static/img/MorphF05_cut_upper.png",
  "app/static/img/MorphF06_cut_upper.png",
  "app/static/img/MorphF07_cut_upper.png",
  "app/static/img/MorphF08_cut_upper.png",
  "app/static/img/MorphF09_cut_upper.png",
  "app/static/img/MorphM01_cut_upper.png",
  "app/static/img/MorphM02_cut_upper.png",
  "app/static/img/MorphM03_cut_upper.png",
  "app/static/img/MorphM04_cut_upper.png",
  "app/static/img/MorphM05_cut_upper.png",
  "app/static/img/MorphM06_cut_upper.png",
  "app/static/img/MorphM07_cut_upper.png",
  "app/static/img/MorphM08_cut_upper.png",
  "app/static/img/MorphM09_cut_upper.png",
  "app/static/img/MorphF01_cut_lower.png",
  "app/static/img/MorphF02_cut_lower.png",
  "app/static/img/MorphF03_cut_lower.png",
  "app/static/img/MorphF04_cut_lower.png",
  "app/static/img/MorphF05_cut_lower.png",
  "app/static/img/MorphF06_cut_lower.png",
  "app/static/img/MorphF07_cut_lower.png",
  "app/static/img/MorphF08_cut_lower.png",
  "app/static/img/MorphF09_cut_lower.png",
  "app/static/img/MorphM01_cut_lower.png",
  "app/static/img/MorphM02_cut_lower.png",
  "app/static/img/MorphM03_cut_lower.png",
  "app/static/img/MorphM04_cut_lower.png",
  "app/static/img/MorphM05_cut_lower.png",
  "app/static/img/MorphM06_cut_lower.png",
  "app/static/img/MorphM07_cut_lower.png",
  "app/static/img/MorphM08_cut_lower.png",
  "app/static/img/MorphM09_cut_lower.png"];


  function preload_img(this_img)
  {
      // load the image
      my_img.src = this_img;
  }

  for (var i = 0; i < all_img.length; i++) {
      preload_img(all_img[i]);
      //alert(all_img[i]);

      if (i >= all_img.length-1){
        setTimeout(function(){$("#startscreen").show();}, 2000 );
        setTimeout( spinner.stop.bind(spinner), 2000);
        }
  }

});
