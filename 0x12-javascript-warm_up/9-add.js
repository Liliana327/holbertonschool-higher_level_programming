#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argument = process.argv;
const a = parseInt(argument[2]);
const b = parseInt(argument[3]);

console.log(add(a, b));
