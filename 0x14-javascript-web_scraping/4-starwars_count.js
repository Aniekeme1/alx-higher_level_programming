#!/usr/bin/node

// Script that prints the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function(error, response, body) {
    if (error) {
        console.log(`An error occurred while making the request: ${error}`);
    } else {
        const jsonData = JSON.parse(body);
        const movies = jsonData.results;
        let count = 0;

        for (let i = 0; i < movies.length; i++) {
            const characters = movies[i].characters;
            for (let j = 0; j < characters.length; j++) {
                if (characters[j].includes('/18/')) {
                    count++;
                    break;
                }
            }
        }

        console.log(`The character Wedge Antilles appears in ${count} movies.`);
    }
});

