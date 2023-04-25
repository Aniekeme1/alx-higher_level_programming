#!/usr/bin/node

// Script that writes a string to a file

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, stringToWrite, 'utf8', function(error) {
    if (error) {
        console.log(`An error occurred while writing the file: ${error}`);
    } else {
        console.log(`The file ${filePath} has been written successfully!`);
    }
});

