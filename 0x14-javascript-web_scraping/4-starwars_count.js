#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const arguments = process.argv;
let url = arguments[2];
let request = require('request');
request(url, function (error, response, body) {
if (error) {
console.log('error:', error); // Print the error if one occurred
} else {
let json = JSON.parse(body);
let results = json['results'];
let count = 0;
for (let i = 0; i < results.length; i++) {
let characters = (results[i]['characters']);
for (let j = 0; j < characters.length; j++) {
let check18 = characters[j].endsWith('18/');
if (check18) {
count++;
}
}
}
console.log(count);
}
});
