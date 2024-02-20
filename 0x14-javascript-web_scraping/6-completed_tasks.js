#!/usr/bin/node
/* Script that computes the number of tasks completed by user id. */
const request = require('request');
const url = process.argv[2];

request(url, function (er, response, body) {
  if (er) {
    console.log(er);
  } else if (response.statusCode === 200) {
    const completed = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
