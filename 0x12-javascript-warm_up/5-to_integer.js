#!/usr/bin/node

const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argument[2]));
}
