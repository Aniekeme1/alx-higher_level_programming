#!/usr/bin/node
// Script that downloads the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

// Make a request to the URL specified in the first argument and pipe the response to a file
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3], { encoding: 'utf8' }));

