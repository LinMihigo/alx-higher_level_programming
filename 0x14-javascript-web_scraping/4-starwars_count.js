#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], { json: true }, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode !== 200) {
        console.log(`Error: ${response.statusCode}`);
    } else {
        const count = body.results.filter(film =>
            film.characters.includes("https://swapi-api.alx-tools.com/api/people/18/")
        ).length;
        console.log(count);
    }
});
