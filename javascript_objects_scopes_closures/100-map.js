#!/usr/bin/node
const listInput = require('./100-data.js').list;
console.log(listInput);
console.log(listInput.map((element, index) => element * index));
