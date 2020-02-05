#!/usr/bin/node

const argument = process.argv;

if (argument[2] == null) {
  console.log('No argument');
} else {
  console.log(argument[2]);
}
