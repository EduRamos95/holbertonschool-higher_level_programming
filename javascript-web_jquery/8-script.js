$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textstatus) => {
    if (textstatus === 'success') {
      const results = data.results;
      for (const movie of results) {
        $('UL#list_movies').append($('<li></li>').text(movie.title));
      }
    }
  });
});
