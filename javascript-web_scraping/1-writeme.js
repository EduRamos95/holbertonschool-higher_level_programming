#!/usr/bin/node
const file = process.argv[2];
const txt = process.argv[3];
const fs = require('fs');
fs.writeFile(file, txt, 'utf8', (err) => {
  if (err) throw err;
});
