#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let new_key;
    let new_value;
    let d_exp = {};
    let d_in = JSON.parse(body);
    for (d_get of d_in) {
      if (d_get["completed"]) {
        new_key = "" + d_get["userId"];
        if (!d_exp[new_key]) {
          d_exp[new_key] = 1;
        } else {
          new_value = d_exp[new_key];
          d_exp[new_key] = new_value + 1;
        }
      }
    }
    console.log(d_exp);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
  });
