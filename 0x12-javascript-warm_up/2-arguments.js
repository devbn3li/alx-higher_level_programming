#!/usr/bin/node
const len = process.argv.length;
console.log(len === 2 ? 'No argument' : len === 3 ? 'Argument found' : 'Arguments found');
