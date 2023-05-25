$(document).ready(function() {
  $('#search-query').keyup(function() {
    var query = $(this).val();
    if (query.length >= 3) {
      $.ajax({
        url: '/user_home/',
        data: { 'q': query },
        dataType: 'json',
        success: function(data) {
          $('#user_home-results').empty();
          $.each(data.data, function(i, obj) {
            var link = $('<a>').attr('href', '/myapp/' + obj.id + '/').text(obj.name);
            var item = $('<li>').append(link);
            $('#user_home-results').append(item);
          });
          $('#user_home-results').show();
        }
      });
    } else {
      $('#user_home-results').hide();
    }
  });
});
