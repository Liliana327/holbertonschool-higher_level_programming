#!/usr/bin/node

// script that prints the number of movies where the character is present.

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    let count = 0;
    for (let a = 0; a < data.length; a++) {
      for (let b = 0; b < data[a].characters.length; b++) {
        if (data[a].characters[b].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Invalid');
  }
});
