#!/usr/bin/node
const number = process.argv[2];

function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return 1;
  }
  return number * factorial(number - 1);
}
console.log(factorial(number));
