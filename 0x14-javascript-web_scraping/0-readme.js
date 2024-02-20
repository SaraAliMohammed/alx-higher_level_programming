#!/usr/bin/node
/* Script that reads and prints the content of a file. */

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (er, data) {
  if (er) {
    console.log(er);
  } else {
    console.log(data);
  }
});
