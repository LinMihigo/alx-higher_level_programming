#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) return console.error(err);
  if (response.statusCode !== 200) {
    return console.error(`Error: Status code ${response.statusCode}`);
  }

  const tasks = JSON.parse(body);
  const completed = tasks.reduce((acc, task) => {
    if (task.completed) acc[task.userId] = (acc[task.userId] || 0) + 1;
    return acc;
  }, {});

  console.log(completed);
});
