#!/usr/bin/node

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');

const message1 = fs.readFileSync(fileA, 'utf-8');
const message2 = fs.readFileSync(fileB, 'utf-8');
const message3 = message1 + message2;
fs.writeFileSync(fileC, message3);
