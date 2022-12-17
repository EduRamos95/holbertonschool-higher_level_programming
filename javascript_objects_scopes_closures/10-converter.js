#!/usr/bin/node
exports.converter = function (base) {
  return x => x.toString(base);
};
