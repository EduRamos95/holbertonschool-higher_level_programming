$(document).ready(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });
  $('DIV#remove_item').click(() => {
    if ($('UL.my_list').has('li').length) {
      $('UL.my_list :last-child').remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
