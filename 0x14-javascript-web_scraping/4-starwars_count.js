#!/usr/bin/node
/* Script that prints the number of movies where
  the character "Wedge Antilles" is present. */
const request = require('request');
const url = process.argv[2];

request(url, function (er, response, body) {
  if (er) {
    console.log(er);
  } else if (response.statusCode === 200) {
    const filmsJson = JSON.parse(body).results;
    let count = 0;
    for (const film of filmsJson) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
