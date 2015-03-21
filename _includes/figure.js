$(document).ready(function() {
  $('.figure-container > a, .gallery-container > a').each(function() {
    $(this).click(function(event) {
      event.preventDefault();
      $('body').hide().prepend('<div class="figure-bg"><figure class="figure-figure"><div class="figure-container"><a class="figure-a"><img class="figure-img"></img></a><figcaption><a target="_blank" href="' + $(this).attr('href') + '">Open in new tab</a></figcaption></div></figure></div>').fadeIn(200);
      $('.figure-img').attr('src', $(this).attr('href'));
      $('.figure-bg').click(function() {
        $('.figure-bg').fadeOut(
            200,
            function() { $(this).remove(); });
      });
    });
  });
});
