#!/usr/bin/node
/* Script that display the status code of a GET request. */
const request = require('request');
const url = process.argv[2];

request(url, function (er, response) {
  if (er) {
    console.log(er);
  } else {
    console.log('code: ', response.statusCode);
  }
});
