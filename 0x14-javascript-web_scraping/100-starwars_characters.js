#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie. */
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (er, response, body) {
  if (er) {
    console.log(er);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characters = movie.characters;
    for (const character of characters) {
      request(character, function (err, res, body2) {
        if (err) {
          console.log(err);
        }
        const characterDetails = JSON.parse(body2);
        console.log(characterDetails.name);
      });
    }
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
