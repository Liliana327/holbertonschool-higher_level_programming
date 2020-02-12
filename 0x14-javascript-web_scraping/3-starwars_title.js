#!/usr/bin/node

// script that prints the title of a Star Wars movie where the episode number

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
