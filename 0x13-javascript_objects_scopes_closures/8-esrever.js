#!/usr/bin/node
exports.esrever = function (list) {
  const revers = [];
  const len = list.length;
  let x = len - 1;
  while (x >= 0) {
    revers.push(list[x]);

    x--;
  }
  return revers;
};
