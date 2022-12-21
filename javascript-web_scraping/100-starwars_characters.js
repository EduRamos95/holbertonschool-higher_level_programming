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
  .then((urlCharacter) => {
    for (const urlChar of urlCharacter) {
      request(urlChar, (err, response, body) => {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.log(`Error: ${response.statusCode}`);
        }
      });
    }
  })
  .catch((err) => { console.log(err); });
