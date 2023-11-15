#!/usr/bin/node
const dict = require('./101-data').dict;
const dictCopy = dict;
const newDictionery = {};

for (const userID in dictCopy) {
  const occurence = dictCopy[userID];
  if (!newDictionery[occurence]) {
    newDictionery[occurence] = [];
  }
  newDictionery[occurence].push(userID);
}
console.log(newDictionery);
