#!/usr/bin/node

// A script that prints a message depending of the number of arguments passed:
// If no arguments are passed to the script, print “No argument”
// If only one argument is passed to the script, print “Argument found”
// Otherwise, print “Arguments found”
// Must use console.log(...) to print all output
// Not allowed to use var

const len = process.argv.length;

if (len < 3) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
