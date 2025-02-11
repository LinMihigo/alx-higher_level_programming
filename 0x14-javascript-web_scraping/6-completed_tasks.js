#!/usr/bin/node
const https = require('https');
const url = process.argv[2];
https.get(url, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    const todos = JSON.parse(data);
    const counts = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        counts[userId] = (counts[userId] || 0) + 1;
      }
    });

    const sortedCounts = Object.fromEntries(
      Object.entries(counts)
        .sort(([a], [b]) => parseInt(a) - parseInt(b))
    );
    console.log(JSON.stringify(sortedCounts, null, 2));
  });
}).on('error', (err) => {
  console.error('Error:', err);
});
