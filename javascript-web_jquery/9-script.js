$(document).ready(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=' + $('html')[0].lang, (data, textstatus) => {
    if (textstatus === 'success') {
      $('DIV#hello').text(data.hello);
    }
  });
});
