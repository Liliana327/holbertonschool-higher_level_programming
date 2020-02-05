#!/usr/bin/node

const argument = process.argv;
if (argument.length < 4) {
  console.log(0);
} else {
  const array = argument.slice(2).sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
