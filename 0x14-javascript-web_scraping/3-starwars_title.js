#!/usr/bin/node
/* Script that prints the title of a Star Wars movie
  where the episode number matches a given integer. */
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, function (er, response, body) {
  if (er) {
    console.log(er);
  } else if (response.statusCode === 200) {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
