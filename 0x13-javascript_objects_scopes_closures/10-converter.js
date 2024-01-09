#!/usr/bin/node

// A function that converts a number from base 10 to another base passed as argument
// Prototype: exports.converter = function (base)

exports.converter = function (base) {
  function conv (number) {
    return number.toString(base);
  }
  return conv;
};
