#!/usr/bin/node
const dictInput = require('./101-data.js').dict;
const dictOut = {};
for (const key in dictInput) {
  if (dictOut[`${dictInput[key]}`] === undefined) {
    dictOut[`${dictInput[key]}`] = [`${key}`];
  } else {
    dictOut[`${dictInput[key]}`].push(`${key}`);
  }
}
console.log(dictOut);
