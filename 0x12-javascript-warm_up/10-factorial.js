#!/usr/bin/node

function factorial (num) {
  if (num <= 1) {
    return (1);
  } else {
    return num * factorial(num - 1);
  }
}
const argument = process.argv;
console.log(factorial(parseInt(argument[2])));
