#!/usr/bin/node

// Script that reads and prints the content of a file

const filePath = process.argv[2];
const fs = require('fs');

// Read the file contents
fs.readFile(filePath, 'utf8', function(error, fileContent) {
    if (error) {
        console.log(`An error occurred while reading the file: ${error}`);
    } else {
        console.log(fileContent);
    }
});

