#!/usr/bin/node

const argument = process.argv;

if (isNaN(argument[2])) {
  console.log('Missing number of occurences');
} else {
  let cont;

  for (cont = 0; cont < argument[2]; cont++) {
    console.log('C is fun');
  }
}
