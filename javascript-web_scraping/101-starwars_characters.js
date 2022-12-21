#!/usr/bin/node
const request = require('request');
const idFilm = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + idFilm;

const myPromise = new Promise((resolve, reject) => {
  request(url, (err, response, body) => {
    if (err) {
      reject(err);
    } else if (response && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      resolve(filmData.characters);
    } else {
      const errorCode = `Error: ${response.statusCode}`;
      reject(errorCode);
    }
  });
});

myPromise
  .then((urlCharacters) => {
    const charOrd = urlCharacters.map(urlChar => {
      return new Promise((resolve, reject) => {
        request(urlChar, (err, response, body) => {
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            const error = `Error: ${response.statusCode}`;
            reject(error);
          }
        });
      });
    });
    return Promise.all(charOrd);
  })
  .then(charOrd => {
    charOrd.forEach(charName => console.log(charName));
  })
  .catch((err) => { console.log(err); });
