#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (er, response, body) {
  if (er) {
    console.log(er);
  } else if (response.statusCode === 200) {
    fs.writeFileSync(filePath, body, 'utf-8');
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
