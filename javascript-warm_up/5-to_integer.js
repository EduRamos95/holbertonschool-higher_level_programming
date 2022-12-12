#!/usr/bin/node
process.argv[2] = parseInt(process.argv[2]);
console.log(Number(process.argv[2]) ? 'My number: ' + process.argv[2] : 'Not a number');
