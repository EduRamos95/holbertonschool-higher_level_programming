$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.get('https://stefanbohacek.com/hellosalut/?lang=' + $('INPUT#language_code').val(), (data, textStatus) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
