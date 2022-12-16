#!/usr/bin/node
exports.esrever = function (list) {
  const index_max = list.length - 1;
  const reverse = [];
  for (let i = index_max; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
