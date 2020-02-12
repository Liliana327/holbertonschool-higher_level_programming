#!/usr/bin/node

// Write a script that computes the number of tasks completed by user id.

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const objts = {};
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      if (objts[data[i].userId] === undefined) {
        objts[data[i].userId] = 1;
      } else {
        objts[data[i].userId]++;
      }
    }
  }
  console.log(objts);
});
