#!/usr/bin/node

const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Missing size');

} else {
  let cont
  for (cont = 0; cont < argument[2]; cont++) {
    console.log(Array(parseInt(argument[2]) + 1).join('X'));
  }
}
