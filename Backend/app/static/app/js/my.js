$(document).ready(function () {
  $(".nav-toggler").on("click", function () {
    console.log("Hello")
    $("navbar-toggler").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });
});

