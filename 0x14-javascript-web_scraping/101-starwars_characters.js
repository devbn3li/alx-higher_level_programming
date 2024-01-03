#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body).characters;
    for (const character of json) {
      request(character, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
}
);
