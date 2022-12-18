#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) throw err;
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
