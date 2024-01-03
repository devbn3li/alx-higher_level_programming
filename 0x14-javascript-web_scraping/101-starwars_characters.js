#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const characterName = JSON.parse(body).name;
          fs.appendFile('characters.txt', characterName + '\n', function (err) {
            if (err) throw err;
          });
        }
      });
    });
  }
}
);
