#!/usr/bin/node

// Script that displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

request.get(url, function(error, response) {
    if (error) {
        console.log(`An error occurred while making the request: ${error}`);
    } else {
        console.log(`code: ${response.statusCode}`);
    }
});

