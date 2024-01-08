#!/usr/bin/node

// A script that searches the second biggest integer in the list of arguments
// Assuming that all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0

if (process.argv.length > 3) {
  const array = process.argv.slice(2).map(Number);

  array.splice(array.indexOf(Math.max.apply(null, array)), 1);
  console.log(Math.max.apply(null, array));
} else {
  console.log(0);
}
