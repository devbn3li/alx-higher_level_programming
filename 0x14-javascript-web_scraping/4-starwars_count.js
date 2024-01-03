#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body).results;
    for (const film of json) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
