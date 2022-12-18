#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let newKey;
    let newValue;
    const dExp = {};
    const dIn = JSON.parse(body);
    for (const dGet of dIn) {
      if (dGet.completed) {
        newKey = '' + dGet.userId;
        if (!dExp[newKey]) {
          dExp[newKey] = 1;
        } else {
          newValue = dExp[newKey];
          dExp[newKey] = newValue + 1;
        }
      }
    }
    console.log(dExp);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
