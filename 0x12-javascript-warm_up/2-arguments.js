#!/usr/bin/node
const count = process.argv.length;
if (count.length === 0) {
    console.log('No argument');
    } else if (count.length === 1) {
    console.log('Argument found');
    }
    else {
    console.log('Arguments found');
    }

console.log(count);
