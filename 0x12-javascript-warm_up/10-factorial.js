#!/usr/bin/node

// A script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// Recursively using a function

function factorial (num) {
  if (num > 0) {
    return num * factorial(num - 1);
  }
  return 1;
}

console.log(factorial(Number(process.argv[2])));
