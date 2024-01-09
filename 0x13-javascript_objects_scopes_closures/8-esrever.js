#!/usr/bin/node

// A function that returns the reversed version of a list
// Prototype: exports.esrever = function (list)

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
