#!/usr/bin/node

// Script that prints the title of a Star Wars movie based on its episode number

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function(error, response, body) {
    if (error) {
        console.log(`An error occurred while making the request: ${error}`);
    } else {
        const movieData = JSON.parse(body);
        console.log(`Title of Star Wars Episode ${movieData.episode_id}: ${movieData.title}`);
    }
});

