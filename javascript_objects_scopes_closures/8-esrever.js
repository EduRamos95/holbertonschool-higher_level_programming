#!/usr/bin/node
exports.esrever = function (list) {
  const indexMax = list.length - 1;
  const reverse = [];
  for (let i = indexMax; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
